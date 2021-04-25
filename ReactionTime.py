from PIL import ImageGrab
from pyautogui import click
from time import sleep

red = (206, 38, 54) #colors taken from site
green = (75, 219, 106)
blue = (43, 135, 209)

while True:
    pixel = ImageGrab.grab(bbox=(400,400,401,401))
    color = pixel.load()
    print(color)
    print(pixel)
    '''if color == green:
        click(x=400, y=400)
    elif color == blue:
        sleep(2)
        click(x=400, y=400)'''
        