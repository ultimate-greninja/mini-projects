import pyautogui
import time
import random
import threading
import keyboard  # You'll need to install this library using `pip install keyboard`

# Disable the fail-safe feature (use with caution)
pyautogui.FAILSAFE = False

# Mapping numbers to keys
key_map = {  
    1: 'z',        # Z is still Z
    2: 'x',        # X is still X
    3: 'up',       # Up arrow is fine
    4: 'down',     # Down arrow is fine
    5: 'left',     # Left arrow is fine
    6: 'right',    # Right arrow is fine
    7: 'enter',    # Enter is still Enter
    8: 'backspace'  # Backspace is still Backspace
}

# Variable to control the autoclicker
is_running = False
is_paused = False  # Variable to track if inputs are paused

# Function to press random keys based on the key_map
def press_random_key():
    global is_paused
    while is_running:
        if not is_paused:  # Only press keys if not paused
            random_number = random.randint(1, 8)  # Pick a random number from 1 to 8
            pressed_key = key_map[random_number]  # Get the mapped key

            # Adjusting print statements to reflect the new mapping
            if pressed_key == 'z':
                print("Pressed B")  # Z mapped to B
            elif pressed_key == 'x':
                print("Pressed A")  # X mapped to A
            elif pressed_key == 'enter':
                print("Pressed Start")  # Enter mapped to Start
            elif pressed_key == 'backspace':
                print("Pressed Select")  # Backspace mapped to Select
            else:
                print(f"Pressed {pressed_key.capitalize()}")  # Print other keys as is

            # Hold down the key for a bit longer
            pyautogui.keyDown(pressed_key)  # Press the key down
            time.sleep(0.2)  # Hold the key down for 0.2 seconds (adjust as needed)
            pyautogui.keyUp(pressed_key)  # Release the key

            # Check for the random number to be 621 to call forfeits()
            if random.randint(1, 100000) == 621:  # Check for 621
                is_paused = True  # Set paused state
                forfeits()  # Call the forfeits function
                is_paused = False  # Resume key presses after forfeit is completed

            time.sleep(random.uniform(0.5, 1.5))  # Add random delay between 0.5 to 1.5 seconds
        else:
            time.sleep(0.1)  # Sleep briefly if paused

# Function to toggle the autoclicker on/off
def toggle_autoclicker():
    global is_running
    if is_running:
        is_running = False
        print("Autoclicker stopped")
    else:
        is_running = True
        print("Autoclicker started")
        threading.Thread(target=press_random_key).start()  # Run the key pressing in a separate thread

# Example usage
def listen_for_toggle():
    print("Press 'Ctrl + ]' to toggle the autoclicker on/off, or 'Esc' to quit.")
    while True:
        if keyboard.is_pressed('ctrl') and keyboard.is_pressed(']'):
            toggle_autoclicker()
            time.sleep(0.5)  # Avoid rapid toggling
        if keyboard.is_pressed('esc'):
            if is_running:
                toggle_autoclicker()  # Ensure it stops before exiting
            print("Program exiting...")
            break

# Start listening for the toggle
listen_for_toggle()
