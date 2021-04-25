from screen_search import *
from pyautogui import click, locateOnScreen

# Search for the github logo on the whole screen
# note that the search only works on your primary screen.
search = Search("images/target.png")

while True: #use ctrl alt delete to stop, if i try to listen for some key to finish or check if finished performance is hindered
    pos = search.imagesearch() #need to find a way to optimize
    if pos[0] != -1:
        click(x=pos[0], y=pos[1])