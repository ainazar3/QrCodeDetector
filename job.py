import cv2
import time
from pynput.keyboard import Controller, Key
import pyautogui
import subprocess
import pyperclip
import threading


keyboard = Controller()
search = None
file = None
SEARCH_FILE = './search.png'
test_name = 'aidana'
FILES = './files.png'

cam = cv2.VideoCapture(0)

cv2.namedWindow("test")

img_counter = 0
timer = 0




def screen():
    while True:
        ret, frame = cam.read()
        if not ret:
            print("failed to grab frame")
            break
        cv2.imshow("test", frame)
        img_name = "frame_{}.png".format(img_counter)

        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))

        break

    cam.release()

    cv2.destroyAllWindows()


screen()
subprocess.call("/home/ainazar/Downloads/Telegram/Telegram")


while search is None:
    search = pyautogui.locateOnScreen(SEARCH_FILE, grayscale=False, confidence=.7)
    time.sleep(1)

pyautogui.moveTo(search)
pyautogui.click()

time.sleep(3)
keyboard.type(test_name)
time.sleep(1)
keyboard.press(Key.enter)
keyboard.release(Key.enter)


time.sleep(5)
while file is None:
    file = pyautogui.locateOnScreen(FILES, grayscale=False, confidence=.7)
    time.sleep(1)


pyautogui.moveTo(file)
pyautogui.click()




time.sleep(5)
keyboard.type('frame_0.png')
time.sleep(1)
keyboard.press(Key.enter)
keyboard.release(Key.enter)



def pressEnter():
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)


time.sleep(5)
pressEnter()


time.sleep(5)
pressEnter()


time.sleep(5)
pressEnter()


time.sleep(5)
pressEnter()


time.sleep(5)
pressEnter()
