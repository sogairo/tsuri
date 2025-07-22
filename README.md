# tsuri

This repository contains the source code for a macro designed for the Roblox game Rune Slayer that automates the fishing profession.

# Table of Contents

- [DISCLAIMER](#disclaimer)
- [Setting up the program](#setting-up-the-program)
- [How to run](#how-to-run)
- [Usage guide](#usage-guide)

# DISCLAIMER

I'm not sure if using this macro is bannable in Rune Slayer, so use it at your own risk. If you get banned for it, that's on you. You've been warned.

# Setting up the program

First, download and install [Visual Studio Code](https://code.visualstudio.com/).

After installing VSCode, install the [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) from the Extensions tab.

Next, download and install the [latest version of Python](https://www.python.org/downloads/).

> You must check the box that says "Add python.exe to PATH" during installation. If you skip this step, the program will not run.

**Once everything is set up, open VSCode's built-in terminal (not your system's terminal) and run the following command:**

```bash
pip install soundcard numpy keyboard
```

# How to Run

Open the script in VSCode.

Press the green play arrow in the top right to run the script.

Once it starts, you'll be prompted in the terminal to enter your audio device index.  
A list of available output devices will appear like this:

```
Available audio output devices:

[0] Speakers (Realtek Audio)
[1] Headphones (USB Audio Device)
[2] Monitor (NVIDIA High Definition Audio)

Enter output device index:
```

Click on the space beside `Enter output device index:` in the terminal and type the number that matches your device (0, 1, 2, etc), then press Enter.

# Usage guide

For best results, use this macro in a quiet area without loud background sounds. Make sure your Roblox volume is set to maximum. Do not play music or any other audio in the background while using this, or it may interfere with detection.

When you run the script in VSCode, follow the instructions shown in the terminal. You will be asked to select your output device. If you choose the wrong one, the program will not work properly as it relies on the system's output device to function.

After selecting your audio device index, switch to the Roblox window and press **P** to start or pause the macro. Press **ESC** to terminate the program. Roblox does not need to be maximized. Running it in windowed mode gives the best results.
