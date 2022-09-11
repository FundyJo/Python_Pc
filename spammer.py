import pyautogui
import keyboard
import time


def send(word):
    while not keyboard.is_pressed("esc"):
        if keyboard.is_pressed("esc"):
            break
        else:
            print(f"Printed '{word}'")
            pyautogui.typewrite(f"{word}")
            pyautogui.press("enter")


print("Starting in 5")
time.sleep(1)
print("Starting in 4")
time.sleep(1)
print("Starting in 3")
time.sleep(1)
print("Starting in 2")
time.sleep(1)
print("Starting in 1")
time.sleep(1)
print("Starting in 0")

send("test")
