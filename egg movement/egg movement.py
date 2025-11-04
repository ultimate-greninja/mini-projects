import pyautogui
import time
import threading
import keyboard  # Requires installation via `pip install keyboard`

# Disable the fail-safe feature (use with caution)
pyautogui.FAILSAFE = False

# Variable to control the movement
is_running = True

# Function to perform left-to-right movement
def move_left_right():
    global is_running
    while is_running:
        # Hold down 'Z' continuously during movement
        pyautogui.keyDown('z')  # Hold down Z key

        # Move left 1 time
        for _ in range(1):
            if not is_running:  # Stop loop if toggled off
                pyautogui.keyUp('z')  # Release Z if stopped
                return
            pyautogui.keyDown('left')
            time.sleep(1)  # Hold the key down for 1 second
            pyautogui.keyUp('left')

        # Move right 1 time
        for _ in range(1):
            if not is_running:  # Stop loop if toggled off
                pyautogui.keyUp('z')  # Release Z if stopped
                return
            pyautogui.keyDown('right')
            time.sleep(1)  # Hold the key down for 1 second
            pyautogui.keyUp('right')

        # Release 'Z' after completing the loop
        pyautogui.keyUp('z')  # Ensure Z is released if the loop ends

# Function to toggle the movement on/off
def toggle_movement():
    global is_running
    if is_running:
        is_running = False
        print("Movement stopped")
    else:
        is_running = True
        print("Movement started")
        threading.Thread(target=move_left_right).start()

# Main function to listen for keyboard inputs
def listen_for_toggle():
    print("Press 'Ctrl + ]' to toggle the movement on/off, or 'Esc' to quit.")
    while True:
        if keyboard.is_pressed('ctrl') and keyboard.is_pressed(']'):
            toggle_movement()
            time.sleep(0.1)  # Avoid rapid toggling
        if keyboard.is_pressed('esc'):
            if is_running:
                toggle_movement()  # Ensure movement stops before exiting
            print("Program exiting...")
            break

# Start listening for toggles
listen_for_toggle()
