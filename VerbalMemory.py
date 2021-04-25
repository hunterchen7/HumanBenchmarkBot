from screen_search import *
from pyautogui import click
from cv2 import imread
from pytesseract import image_to_string
from time import sleep

words = []

start = Search("images/verbalStart.png").imagesearch()

if start[0] != -1:
    click(x=start[0], y=start[1])

sleep(1)

print('hold on..')

topLeft = Search("images/verbalLives.png").imagesearch() #top left is left of "Lives"
left = topLeft[0]
top = topLeft[1]
botRight = Search("images/verbalNew.png").imagesearch() #bottom right signified by "NEW" button
right = botRight[0]
bottom = botRight[1]

sleep(1)
print('hold on...')

seen = Search("images/seenButton.png").imagesearch()
new = Search("images/newButton.png").imagesearch()

while True: #makes mistakes sometimes but I don't know where or how
    sleep(0.1) #pauses to let page load
    pyautogui.screenshot(region=(left, top + 50, right - left + 100, bottom - top - 50)).save("images/word.png")
    img = imread("images/word.png")
    word = image_to_string(img) #this is really inaccurate for whatever reason
    print(words)
    print(word)
    if word in words:
        pyautogui.click(x=seen[0],y=seen[1])
    else:
        words.append(word)
        pyautogui.click(x=new[0],y=new[1])