from screen_search import *
from pyautogui import click, screenshot, moveTo, locateAll
from time import sleep
from PIL import ImageGrab, Image

im = Image.open('images/seq.png')
print(im.getpixel((30,30)))