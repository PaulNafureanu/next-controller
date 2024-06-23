import pyautogui
from utils import AutoguiUtils


def sec():
    pyautogui.sleep(1)
    pyautogui.hotkey("alt", "c")

    pyautogui.sleep(0.1)
    pyautogui.hotkey("ctrl", "enter")

    pyautogui.sleep(0.1)
    pyautogui.hotkey("ctrl", "enter")

    pyautogui.sleep(0.1)
    pyautogui.press("down")
    pyautogui.press("down")
    pyautogui.press("down")
    pyautogui.sleep(1)
    AutoguiUtils.insertText("Andrei")

    pyautogui.sleep(1)
    pyautogui.press("enter")

    pyautogui.sleep(1)
    pyautogui.press("enter")

    pyautogui.sleep(1)
    pyautogui.press("enter")

    pyautogui.sleep(1)
    AutoguiUtils.insertText("as231")

    pyautogui.sleep(1)
    pyautogui.press("enter")

    pyautogui.sleep(1)
    pyautogui.press("enter")

    pyautogui.sleep(1)
    pyautogui.press("enter")
    # pyautogui.hotkey("shift","insert")
