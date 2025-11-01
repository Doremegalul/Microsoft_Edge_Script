# === Instructions ===
# Put this in cmd: .\.venv\Scripts\Activate
# Then put this: Python auto_search.py
# ====================

import pyautogui
import pyperclip
import time
import random
import re

def get_random_sentence(file_path: str, min_length: int = 30) -> str:
    """
    Load a text file, split it into sentences, and return a random sentence 
    with at least `min_length` visible (non-space) characters.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    # Split text into sentences (handles '.', '?', '!')
    sentences = re.split(r'(?<=[.!?])\s+', text)

    # Filter sentences that have `min_length` visible characters (no spaces)
    valid_sentences = [s for s in sentences if len(s.replace(" ", "")) >= min_length]

    if not valid_sentences:
        raise ValueError(f"No sentence with {min_length}+ visible characters found in file!")

    selected = random.choice(valid_sentences).strip()
    print(f"Selected sentence ({len(selected)} chars):\n{selected}\n")

    return selected

def run_auto_search(text: str):
    """
    Automate opening Microsoft Edge, clicking the search bar,
    pasting the given text, and pressing Enter.
    """
    # STEP 1: Click on Microsoft Edge icon (bottom taskbar)
    pyautogui.click(251, 1057)  # Update these coordinates if Edge is moved. See mouse_coordinates.py.
    time.sleep(2)

    # STEP 2: Click on the search bar
    pyautogui.click(1123, 243)
    time.sleep(2)

    # STEP 3: Paste the text and press Enter
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl", "v")
    time.sleep(0.3)
    pyautogui.press("enter")

    print("Initial search triggered!")  # Confirmation
    time.sleep(2)

def delete_and_search_loop(text: str, max_deletions: int = 30):
    """
    Repeatedly delete characters from the search bar.
    For visible characters: backspace, press Enter, wait 10s, and count it.
    For invisible/space characters: just backspace (no Enter, no wait, no count).
    """
    INVISIBLE_CHARS = ["\u200b", "\u200c", "\u200d", "\ufeff"]  # Common invisible Unicode characters

    count = 0
    pos = len(text) - 1  # start from the end of the text
    attempts = 0 # A failed safe

    print(f"Starting loop — will perform up to {max_deletions} visible deletions.")

    while count < max_deletions and pos >= 0:
        next_char = text[pos]

        if not (next_char.isspace() or next_char in INVISIBLE_CHARS):
            # Click search bar only for visible characters
            pyautogui.click(600, 121)
            time.sleep(0.2)

            # Delete visible character
            pyautogui.press("backspace")
            time.sleep(0.05)
            pyautogui.press("enter")
            count += 1
            print(f"Deleted visible char '{next_char}' (position {pos}). Total deletions: {count}")
            time.sleep(10)
        else:
            # Invisible or space: just backspace, no click, no enter, no wait
            pyautogui.press("backspace")
            time.sleep(0.05)
            print(f"Skipped invisible/space char at position {pos}.")

        pos -= 1  # always move to the previous character
        attempts += 1

        # Emergency eject, something went wrong!!!
        if attempts > 40:
            break

    print("Delete loop completed.")


def main():
    # Countdown timer from 5 seconds to allow you to be prepared. 
    # Do not move the mouse during this time. Or else you are stinky and screwed.
    for i in range(5, 0, -1):
        print(f"Starting in {i} seconds...")
        time.sleep(1)
    print("Starting automation now!")

    # Load a random sentence from your file
    FILE_PATH = "bee movie script.txt"
    TEXT = get_random_sentence(FILE_PATH)

    # Run the initial search automation
    run_auto_search(TEXT)

    # Perform the delete-and-search loop (30 visible deletions)
    delete_and_search_loop(TEXT, max_deletions=30)

if __name__ == "__main__":
    main()