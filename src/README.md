<b>Retina</b>

A cross-platfrom utility using eye tracking and pose estimation to play/pause videos based on if the user is looking at/awayfrom the screen.

Dependencies:

1.`OpenCV` v3

2.`psutils` for process management

3.`pyautogui` for GUI automation

Currently supports VLC Media Player only.

Configuration:

Although not necessary, I've set my VLC hotkey for "pause only" as `Shift+1`
and "play only" as `Shift+2`, to avoid ambiguity among other hotkeys. Recommended to do this.


Retina must be running in the background, while using VLC. Moving the .pyw file to the system startup folder may be done, or a .BAT file which executes both, VLC and `Retina.pyw`

