import keyboard
import os
while True:
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN and event.name == 'sleep':
        os.startfile(r"C:\WINDOWS\system32\Taskmgr.exe")

