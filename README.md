# tsuri

This repository contains the source code for a macro designed for the Roblox game Rune Slayer that automates the fishing profession.

> [!CAUTION]
> I'm not sure if using this macro is bannable in Rune Slayer, so use it at your own risk. If you get banned for it, that's on you. You've been warned.

# Table of Contents

- [Setting up the program](#setting-up-the-program)
- [How to run](#how-to-run)
- [Usage guide](#usage-guide)

# Setting up the program

First, download and install [Visual Studio Code](https://code.visualstudio.com/).

After installing VSCode, install the [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) from the Extensions tab.

Next, download and install the [latest version of Python](https://www.python.org/downloads/).

> [!IMPORTANT]
> You must check the box that says "☐ Add python.exe to PATH" during installation. If you skip this step, the program will not run.

Once everything is set up, open VSCode's built-in terminal by pressing `Ctrl + \`` (not your system's terminal) and run the following command:

```bash
pip install soundcard numpy keyboard
```
> [!WARNING]
> This command will not work if Python was not added to PATH during installation.


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

> [!TIP]
> If you're not sure which one to use, test each device to see which one emits the Roblox game sound.

# Usage guide

For best results, use this macro in a quiet area without loud background sounds. Make sure your Roblox volume is set to maximum. Do not play music or any other audio in the background while using this, or it may interfere with detection.

When you run the script in VSCode, follow the instructions shown in the terminal. You will be asked to select your output device. If you choose the wrong one, the program will not work properly as it relies on the system's output device to function.

After selecting your audio device index, switch to the Roblox window and press **P** to start or pause the macro. Press **ESC** to terminate the program. Roblox does not need to be maximized. Running it in windowed mode gives the best results.

> [!IMPORTANT]
> You must be holding the fishing rod and hovering your mouse over water when you press P, or the macro will not work correctly.
