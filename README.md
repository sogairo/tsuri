# tsuri

This repository contains the source code for a macro designed for the Roblox game Rune Slayer that automates the fishing profession.

> [!CAUTION]
> Using macros might be bannable in Rune Slayer, so use it at your own risk. If you get banned for it, my condolences. You've been warned.
<br>

# Table of Contents

- [Setting up the program](#setting-up-the-program)
- [Usage guide](#usage-guide)
<br>

# Setting up the program

Download and install the following onto your system:
1. [Visual Studio Code](https://code.visualstudio.com/) and this [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) right after installing VSCode
2. [The latest version of Python](https://www.python.org/downloads/)
<br>

> [!IMPORTANT]
> You must check the box that says "☐ Add python.exe to PATH" during installation. If you skip this step, the next steps within VSCode will NOT work.
<br>
<br>

Within VSCode, run the following command by using <ins>VSCode's built-in terminal</ins> (`Ctrl + \`):
1. `pip install soundcard numpy keyboard`
<br>

> [!WARNING]  
> This command will not work if Python was not added to PATH during installation. If you messed this up, uninstall Python using the same installer and reinstall it. Make sure to check the box to add it to PATH.
<br>
<br>

Also within VSCode, follow the following steps to fix the `fromstring()` error: 
1. Paste this into the terminal to find the install location:
   ```
   pip show soundcard
   ```
   You’ll see something like:
   ```
   C:\Users\<USER>\AppData\Local\Programs\Python\Python313\Lib\site-packages
   ```

2. Copy that `Location` path and add `\soundcard\mediafoundation.py` to the end of it. It should look like this:
   ```
   C:\Users\<USER>\AppData\Local\Programs\Python\Python313\Lib\site-packages\soundcard\mediafoundation.py
   ```

3. Paste that full path into the `Ctrl + P` search bar in VSCode to open the file directly.

4. Replace line 761 with:
   ```python
   chunk = numpy.frombuffer(_ffi.buffer(data_ptr, nframes*4*len(set(self.channelmap))), dtype='float32')
   ```

5. Save the file and close it. (`Ctrl + S`)
<br>

> [!NOTE]
> This fixes the `ValueError` caused by using `fromstring()` in NumPy 2.x.
<br>

# Usage guide

Open the script in VSCode and press the green play arrow in the top right to run it.

Follow the terminal instructions to select your output device. If you choose the wrong one, the macro won't work since it relies on system audio.
<br>

> [!TIP]  
> If you're not sure which output device to select, test each one or look it up in the Windows Sound settings to find the one playing Roblox audio.
<br>

Once selected, go to the Roblox window, equip your fishing rod, and hover your mouse over water. Make sure you are in first-person view and facing downward at the water. Then press **P** to start or pause the macro. Press **ESC** to stop it. Windowed mode works best.
<br>

> [!TIP]  
> Use this macro in a quiet area with no loud background sounds. Set your Roblox volume to maximum. Avoid playing music or other audio while it's running.
