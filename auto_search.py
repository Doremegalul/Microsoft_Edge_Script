import pyautogui
import pyperclip
import time

# === CONFIGURATION ===
# Put this in cmd: .\.venv\Scripts\Activate

#TEXT = "ExampleSearchQueryThatIsDefinitelyLongerThanThirtyCharacters"
TEXT = ""
INTERVAL_DELETE = 10       # wait before next deletion
MIN_LENGTH = 1
SEARCH_BAR_X = 600
SEARCH_BAR_Y = 121
TIMER_BEFORE_START = 5
# ======================

# Countdown timer
for i in range(TIMER_BEFORE_START, 0, -1):
    print(f"Starting in {i} seconds...")
    time.sleep(1)

print("Starting automation now!")

# Focus and paste text
pyautogui.click(SEARCH_BAR_X, SEARCH_BAR_Y)
time.sleep(0.5)
pyperclip.copy(TEXT)
pyautogui.hotkey("ctrl", "v")
time.sleep(0.3)
pyautogui.press("enter")
print("Initial search triggered!")

time.sleep(3)

# Loop for deletion
current_length = len(TEXT)
print(f"Starting length: {current_length}, will stop at {MIN_LENGTH}")

while current_length > MIN_LENGTH:
    print(f"⏳ Waiting {INTERVAL_DELETE}s before next delete...")
    time.sleep(INTERVAL_DELETE)

    # Focus, delete, and search again
    pyautogui.click(SEARCH_BAR_X, SEARCH_BAR_Y)
    time.sleep(0.2)
    pyautogui.press("backspace")
    pyautogui.press("enter")

    current_length -= 1
    print(f"Deleted 1 char and pressed Enter. Remaining: {current_length}")

print("✅ Finished deleting down to 30 characters.")
