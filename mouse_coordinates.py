import pyautogui
import time

# Move the mouse to the destinated area within 5 seconds to get its coordinates
print("Move your mouse over the destinated area within 5 seconds...")
time.sleep(5)

# Get and print the mouse coordinates
x, y = pyautogui.position()
print(f"Mouse coordinates: ({x}, {y})")