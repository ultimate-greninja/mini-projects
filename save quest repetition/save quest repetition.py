import pyautogui
import time
import threading
import keyboard  # Requires installation via `pip install keyboard`

# Disable the fail-safe feature (use with caution)
pyautogui.FAILSAFE = False

# Variable to control the movement
is_running = True

# Function to perform the key press sequence
def press_x_twice_enter():
    global is_running
    for _ in range(24):  # Repeat 40 times
        if not is_running:  # Stop loop if toggled off
            return
        pyautogui.press('enter')  # Press 'enter' key
        pyautogui.press('x')  # Press 'x' key once
        pyautogui.press('x')  # Press 'x' key again
        time.sleep(2)  # Wait a moment before repeating (adjust as needed)

# Function to toggle the movement on/off
def toggle_movement():
    global is_running
    if is_running:
        is_running = False
        print("Sequence stopped")
    else:
        is_running = True
        print("Sequence started")
        threading.Thread(target=press_x_twice_enter).start()

# Main function to listen for keyboard inputs
def listen_for_toggle():
    print("Press 'Ctrl + ]' to toggle the sequence on/off, or 'Esc' to quit.")
    while True:
        if keyboard.is_pressed('ctrl') and keyboard.is_pressed(']'):
            toggle_movement()
            time.sleep(0.5)  # Avoid rapid toggling
        if keyboard.is_pressed('esc'):
            if is_running:
                toggle_movement()  # Ensure sequence stops before exiting
            print("Program exiting...")
            break

# Start listening for toggles
listen_for_toggle()
