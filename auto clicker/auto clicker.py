import pyautogui
import time
import threading
import keyboard  # For detecting key presses
import random

pyautogui.FAILSAFE = False

# Time between clicks in seconds (adjustable)
default_delay = 0.5
num_clicks = None  # Set to None for infinite clicks
clicking = False  # Track the state of the auto-clicker
lock = threading.Lock()  # Prevent race conditions when modifying `clicking`

def auto_clicker():
    count = 0
    while True:
        with lock:
            if clicking:
                if num_clicks is None or count < num_clicks:
                    pyautogui.click()
                    count += 1
                    time.sleep(random.uniform(0.1,0.3))  # Random delay between clicks
                else:
                    break  # Stop clicking if limit is reached
            else:
                time.sleep(0.1)  # Reduce CPU usage when paused

def toggle_clicking():
    global clicking
    with lock:
        clicking = not clicking
    print("Auto-clicker started!" if clicking else "Auto-clicker stopped!")

# Set the keybind to toggle the auto-clicker (CTRL + ] in this case)
keyboard.add_hotkey('ctrl+]', toggle_clicking)

# Run the auto-clicker in a separate thread
clicker_thread = threading.Thread(target=auto_clicker, daemon=True)
clicker_thread.start()

print("Press CTRL+] to start/stop the auto-clicker.")
print("Press ESC to exit.")

# Wait for 'Esc' key to exit
keyboard.wait('esc')

