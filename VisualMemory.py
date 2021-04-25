from screen_search import *
from pyautogui import click, screenshot, moveTo, locateAll
from time import sleep
from PIL import ImageGrab, Image

start = Search('images/visStart.png').imagesearch()
col_white = (255,255,255)

if start[0] != -1:
    click(x=start[0], y=start[1])

moveTo(1,1)

#hardcoded because the other way was wacky and required too much work
left = 750
top = 250
bottom = 650
right = 1155

def get_first_white(): #assume one can always be found
    # returns a tuple as (left, top, right, bottom)
    im = Image.open('images/seq.png')
    w, h = im.size
    #print(w,h)
    left, top, right, bottom = 0, 0, 0, 0
    for i_x in range(w):
        for i_y in range(h):
            #print(i_x, i_y)
            p_color = im.getpixel((i_x, i_y))
            #print(i_x, i_y, p_color)
            if p_color == col_white:
                #print(i_x, i_y) 
                left, top = i_x, i_y
                break
        if p_color == col_white:
            break

    #print(left, top)

    for i_x in range(i_x, w):
        #print('ix')
        p_color = im.getpixel((i_x, top))
        #p_color = im.load()[i_x,top]
        if p_color != col_white: 
            right = i_x
            break
    for i_y in range(i_y, h):
        #print('iy')
        p_color = im.getpixel((left,i_y))
        if p_color != col_white: 
            bottom = i_y
            break

    #print('first white:', left, top, right, bottom)
    return(left, top, right, bottom)
    #screenshot(region=(left, top, right - left, bottom - top)).save('images/seqWhite.png')

while True:
    sleep(0.75)
    seq = screenshot(region=(left, top, right-left, bottom-top))
    seq.save('images/seq.png') # the actual sequence
    r_left, r_top, r_right, r_bottom = get_first_white() # r for relative, because coords are relative to seq.png not the entire screen
    screenshot(region=(r_left + left - 1, r_top + top - 8, r_right - r_left + 1, r_bottom - r_top + 15)).save('images/seqWhite.png') #saves the white square
    sleep(0.25)
    whites = [tuple(i) for i in locateAll('images/seqWhite.png', 'images/seq.png')]
    print(len(whites), "white tiles located at", whites)
    click(x=1, y=1) #mock click
    sleep(0.5)
    
    for tile in whites:
        x = left + tile[0] + tile[2] // 2
        y = top + tile[1] + tile[3] // 2
        click(x=x, y=y)
    
    sleep(1)