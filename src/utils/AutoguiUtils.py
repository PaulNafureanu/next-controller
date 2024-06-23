import pyautogui


def insertText(text: str, delay: int = 0.1):
    index = 0
    copy = text
    while index < len(copy):
        pyautogui.press(copy[index])
        pyautogui.sleep(delay)
        index += 1
