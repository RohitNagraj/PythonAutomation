# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 17:00:26 2018

@author: rohit
"""

from PIL import ImageGrab, ImageOps
import pyautogui
import time
import numpy as np


class coordinates():
    replayBtn = (342, 312)
    dinoNose = (82, 318)
    # 157,360


def restartGame():
    pyautogui.click(coordinates.replayBtn)


def pressSpace():
    pyautogui.keyDown('space')
    time.sleep(0.05)
    print('JUMP')
    pyautogui.keyUp('space')


def imageGrab():
    box = (coordinates.dinoNose[0]+28, coordinates.dinoNose[1]+6,
           coordinates.dinoNose[0]+118, coordinates.dinoNose[1]+32)
    image = ImageGrab.grab(box)
    greyImage = ImageOps.grayscale(image)
    a = np.array(greyImage.getcolors())
    return(a.sum())


restartGame()
while True:
    x = imageGrab()
    if x != 2595 and x != 2340:
        pressSpace()

    # if a.
#2595, clear
#2678, not clear
