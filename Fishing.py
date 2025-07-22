import soundcard as sc
import numpy as np
import time
import keyboard
import ctypes
import sys

# === CONFIG ===
SAMPLE_RATE = 44100
FRAME_DURATION = 0.03
SOUND_THRESHOLD = 0.015
PLOP_THRESHOLD = 0.012
SPLASH_TIMEOUT = 1.7
CAST_INTERVAL = 0.5
SPLASH_INIT_DELAY = 0.08
MIN_BITE_DELAY = 0.5

MOUSEEVENTF_LEFTDOWN = 0x0002
MOUSEEVENTF_LEFTUP = 0x0004

# === GLOBAL STATE ===
started = False
paused = False
pause_start_time = None
total_pause_duration = 0
program_start_time = None
paused_runtime = 0
last_event_time_adjusted = None
detection_count = 0

def adjusted_time():
    if program_start_time is None:
        return 0
    now = time.time()
    live_pause = (now - pause_start_time) if paused and pause_start_time else 0
    return now - program_start_time - total_pause_duration - live_pause

def win32_mouse_click():
    ctypes.windll.user32.mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    time.sleep(0.065)
    ctypes.windll.user32.mouse_event(MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

def toggle_pause():
    global paused, pause_start_time, started, program_start_time, total_pause_duration, paused_runtime
    if not started:
        started = True
        paused = False
        program_start_time = time.time()
        total_pause_duration = 0
        print()
        print_debug_block()
        update_debug(0.0, detection_count, mic.name, "Running", "Idle")
    else:
        paused = not paused
        if paused:
            pause_start_time = time.time()
            paused_runtime = adjusted_time()
            update_debug(0.0, detection_count, mic.name, "Paused", "Idle")
        else:
            if pause_start_time:
                total_pause_duration += time.time() - pause_start_time
                pause_start_time = None

def check_keys():
    if keyboard.is_pressed("esc"):
        if started:
            update_debug(0.0, detection_count, mic.name, "Terminated", "Idle")
        sys.exit()
    if keyboard.is_pressed("p"):
        toggle_pause()
        time.sleep(0.2)

def update_debug(volume, detection_count, mic_name, status, phase):
    current_runtime = paused_runtime if paused else adjusted_time()
    h, m, s = int(current_runtime // 3600), int((current_runtime % 3600) // 60), int(current_runtime % 60)
    runtime_str = f"{h:02}:{m:02}:{s:02}"

    if last_event_time_adjusted is None:
        bite_str = "0.0 seconds"
    else:
        time_since_last = max(0, current_runtime - last_event_time_adjusted)
        if time_since_last < 60:
            bite_str = f"{time_since_last:.1f} seconds"
        else:
            mins = int(time_since_last // 60)
            secs = int(time_since_last % 60)
            bite_str = f"{mins} min {secs} sec"

    sys.stdout.write("\033[7F")
    sys.stdout.write(
        f"RMS Level:              {volume:.3f}               \n"
        f"Fish Caught:            {detection_count:<10}      \n"
        f"Time Since Last Bite:   {bite_str:<24}\n"
        f"Status:                 {status:<24}\n"
        f"Fishing:                {phase:<24}\n"
        f"Mic:                    {mic_name:<48}\n"
        f"Runtime:                {runtime_str:<10}\n"
    )
    sys.stdout.flush()

def print_debug_block():
    print("RMS Level:              ")
    print("Fish Caught:            ")
    print("Time Since Last Bite:   ")
    print("Status:                 ")
    print("Fishing:                ")
    print("Mic:                    ")
    print("Runtime:                ")

# === MIC SELECTION ===
print("Available audio input devices:\n")
mics = sc.all_microphones(include_loopback=True)
for i, mic in enumerate(mics):
    print(f"[{i}] {mic.name}")

mic_index = int(input("\nEnter input device index: "))
mic = mics[mic_index]

print(f"\n[INFO] Using: {mic.name}")
print("[INFO] Press [P] to begin. Press [ESC] to quit.")

while not started:
    check_keys()
    time.sleep(0.01)

# === MAIN LOOP ===
try:
    while True:
        check_keys()
        if paused:
            update_debug(0.0, detection_count, mic.name, "Paused", "Idle")
            time.sleep(0.05)
            continue

        win32_mouse_click()
        time.sleep(SPLASH_INIT_DELAY)

        splash_detected = False
        splash_start = time.time()
        max_volume_seen = 0
        spike_count = 0
        low_volume_frames = 0

        MIN_SPLASH_TIME = 0.2
        MAX_SPLASH_TIME = 1.3

        while time.time() - splash_start < SPLASH_TIMEOUT:
            check_keys()
            if paused:
                update_debug(0.0, detection_count, mic.name, "Paused", "Idle")
                time.sleep(0.05)
                continue

            since_cast = time.time() - splash_start
            data = mic.record(samplerate=SAMPLE_RATE, numframes=int(SAMPLE_RATE * 0.015))
            if len(data.shape) > 1:
                data = np.mean(data, axis=1)
            volume = np.sqrt(np.mean(data**2))
            max_volume_seen = max(max_volume_seen, volume)

            update_debug(volume, detection_count, mic.name, "Running", "Listening for Splash")

            if since_cast < MIN_SPLASH_TIME:
                continue
            if since_cast > MAX_SPLASH_TIME:
                break

            if volume > PLOP_THRESHOLD:
                spike_count += 1
                low_volume_frames = 0
            else:
                if spike_count > 0:
                    low_volume_frames += 1

            if spike_count >= 2 and low_volume_frames >= 2:
                splash_detected = True
                last_event_time_adjusted = adjusted_time()
                break

            time.sleep(0.005)

        if not splash_detected:
            update_debug(max_volume_seen, detection_count, mic.name, "Retrying", "No Plop Sound")
            time.sleep(1.0)
            continue

        update_debug(0.0, detection_count, mic.name, "Running", "Waiting for Bite")
        bite_start = time.time()
        bite_grace_end = bite_start + MIN_BITE_DELAY
        high_count = 0

        while True:
            if time.time() - bite_start >= 60:
                update_debug(0.0, detection_count, mic.name, "Timeout", "Skipped Bite")
                time.sleep(1.0)
                break

            check_keys()
            if paused:
                update_debug(0.0, detection_count, mic.name, "Paused", "Idle")
                time.sleep(0.05)
                continue

            data = mic.record(samplerate=SAMPLE_RATE, numframes=int(SAMPLE_RATE * FRAME_DURATION))
            if len(data.shape) > 1:
                data = np.mean(data, axis=1)
            volume = np.sqrt(np.mean(data**2))

            update_debug(volume, detection_count, mic.name, "Running", "Waiting for Bite")

            if time.time() < bite_grace_end:
                continue

            if volume > SOUND_THRESHOLD:
                high_count += 1
            else:
                high_count = max(0, high_count - 1)

            if high_count >= 2:
                win32_mouse_click()
                detection_count += 1
                last_event_time_adjusted = None
                update_debug(volume, detection_count, mic.name, "Running", "Caught!")

                flush_start = time.time()
                while time.time() - flush_start < 0.3:
                    check_keys()
                    mic.record(samplerate=SAMPLE_RATE, numframes=int(SAMPLE_RATE * FRAME_DURATION))

                time.sleep(CAST_INTERVAL)
                break

except KeyboardInterrupt:
    if started:
        update_debug(0.0, detection_count, mic.name, "Terminated", "Idle")
    sys.exit()
