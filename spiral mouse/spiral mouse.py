import pyautogui
import math
import time

# ---- startup delay so you can switch tabs ----
print("Starting in 2 seconds...")
time.sleep(2)

pyautogui.PAUSE = 0.002
pyautogui.FAILSAFE = True

# Screen center
width, height = pyautogui.size()
center_x = width // 2
center_y = height // 2

pyautogui.moveTo(center_x, center_y, duration=0.4)

# ---- spiral settings ----
radius = min(width, height) // 1.5   # fixed size of spiral
turns = 250                           # coils within each pass
points = 2500                       # smoothness
repeats = 5
rotation_step = math.radians(231.5)  # rotate each repeat by 51.5°

def spiral_point(t, rotation):
    angle = turns * 2 * math.pi * t + rotation
    r = radius * t                  # spiral from center outward

    x = center_x + r * math.cos(angle)
    y = center_y + r * math.sin(angle)
    return x, y

for loop in range(repeats):

    rotation = loop * rotation_step

    # outward spiral
    for i in range(points):
        t = i / points
        pyautogui.moveTo(*spiral_point(t, rotation))

    time.sleep(0.2)

    # inward spiral (same rotation)
    for i in reversed(range(points)):
        t = i / points
        pyautogui.moveTo(*spiral_point(t, rotation))

    time.sleep(0.2)