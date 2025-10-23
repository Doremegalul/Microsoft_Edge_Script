import pyautogui
import pyperclip
import time

# === CONFIGURATION ===
# Put this in cmd: .\.venv\Scripts\Activate

TEXT = "ExampleSearchQueryThatIsDefinitelyLongerThanThirtyCharacters"
#TEXT = ""
INTERVAL_DELETE = 10       # wait before next deletion
MIN_LENGTH = 1
# ======================

# Countdown timer from 5 seconds
for i in range(5, 0, -1):
    print(f"Starting in {i} seconds...")
    time.sleep(1)
print("Starting automation now!")

# Setting up everything
# STEP 1: Initial click to open microsoft edge at the bottom
pyautogui.click(251, 1057) # NOTE: If you are moving the microsoft edge icon, update these coordinates
time.sleep(0.5)

# STEP 2: Click on the search bar
pyautogui.click(1123, 243)
time.sleep(0.5)

# STEP 3: Paste the text and press enter
pyperclip.copy(TEXT)
pyautogui.hotkey("ctrl", "v")
time.sleep(0.3)
pyautogui.press("enter")
print("Initial search triggered!") # If printed, means everything is setup correctly
#time.sleep(3)

# STEP 4: The loop of deleting and searching again
count = 0
MAX_DELETIONS = 30  # number of times to delete and search
print(f"Starting loop — will delete {MAX_DELETIONS} characters.")

# Run exactly 30 delete/search cycles
while count < MAX_DELETIONS:
    print(f"⏳ Waiting {INTERVAL_DELETE}s before next delete ({count + 1}/{MAX_DELETIONS})...")
    time.sleep(INTERVAL_DELETE)

    # Focus, delete, and search again
    pyautogui.click(600, 121)
    time.sleep(0.2)
    pyautogui.press("backspace")
    pyautogui.press("enter")

    count += 1
    print(f"Deleted {count} char(s) and pressed Enter.")

print("✅ Finished 30 delete-search cycles.")

