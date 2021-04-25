from PIL import ImageGrab
from pyautogui import click
from time import sleep

#colors taken from site
red = (206, 38, 54) 
green = (75, 219, 106)
blue = (43, 135, 209)

while True:
    color = ImageGrab.grab().getpixel((400, 400)) 
    #getpixel() seems to be about 20% faster than load() but they're both inconsistent enough that I'd need to test more
    if color == green:
        click(x=400, y=400)
    elif color == blue:
        sleep(1)
        click(x=400, y=400)
        