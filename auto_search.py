import pyautogui
import pyperclip
import time
import random
import re

# === CONFIGURATION ===
# Put this in cmd: .\.venv\Scripts\Activate

FILE_PATH = "bee movie script.txt"
INTERVAL_DELETE = 10
MAX_DELETIONS = 30
# ======================

# STEP 0: Load and pick a random valid sentence
with open(FILE_PATH, "r", encoding="utf-8") as f:
    text = f.read()

# Split text into sentences (handles '.', '?', '!')
sentences = re.split(r'(?<=[.!?])\s+', text)

# Filter sentences that have 30+ visible characters (no spaces)
valid_sentences = [s for s in sentences if len(s.replace(" ", "")) >= 30]

if not valid_sentences:
    raise ValueError("No sentence with 30+ visible characters found in file!")

TEXT = random.choice(valid_sentences).strip()
print(f"✅ Selected sentence ({len(TEXT)} chars):\n{TEXT}\n")

# Countdown timer from 5 seconds
for i in range(5, 0, -1):
    print(f"Starting in {i} seconds...")
    time.sleep(1)
print("Starting automation now!")

# STEP 1: Initial click to open microsoft edge at the bottom
pyautogui.click(251, 1057) # NOTE: If you are moving the microsoft edge icon, update these coordinates
time.sleep(2)

# STEP 2: Click on the search bar
pyautogui.click(1123, 243)
time.sleep(2)

# STEP 3: Paste the text and press enter
pyperclip.copy(TEXT)
pyautogui.hotkey("ctrl", "v")
time.sleep(0.3)
pyautogui.press("enter")
print("Initial search triggered!") # If printed, means everything is setup correctly
time.sleep(2)

# STEP 4: The loop of deleting and searching again
count = 0
print(f"Starting loop — will perform {MAX_DELETIONS} delete cycles.")

while count < MAX_DELETIONS:
    print(f"⏳ Waiting {INTERVAL_DELETE}s before next delete ({count + 1}/{MAX_DELETIONS})...")
    time.sleep(INTERVAL_DELETE)

    pyautogui.click(600, 121)
    time.sleep(0.2)

    # Check if next char to delete is space/invisible
    if count < len(TEXT) and TEXT[-(count+1)].isspace():
        pyautogui.press("backspace")
        print(f"Skipped space/invisible at position {len(TEXT)-(count+1)}")
        continue  # don’t count it or press enter

    pyautogui.press("backspace")
    pyautogui.press("enter")

    count += 1
    print(f"Deleted {count} char(s) and pressed Enter.")

print("✅ Finished delete-search cycles.")

