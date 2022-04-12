from time import sleep
import pyautogui as pt
import pyperclip as pc

sleep(2)

def MoveToSpeker(message):
    position = pt.locateOnScreen('Assets/spek.png', confidence=.7)
    pt.moveTo(position[0:2], duration=.5)

MoveToSpeker('hello')

