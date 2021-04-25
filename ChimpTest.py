from screen_search import *

num_pos = []

start = Search("images/startChimp.png").imagesearch()
pyautogui.click(x=start[0],y=start[1]) #start test
cont = Search("images/chimpContinue.png")

while True:
    cont_pos = cont.imagesearch()
    if cont_pos[0] != -1:
        pyautogui.click(x=cont_pos[0],y=cont_pos[1])
        pyautogui.moveTo(1,1) #moves to corner as to not obstruct things
    else:
        for i in range(1,21):
            im = Search("images/%d.png" % (i))
            pos = im.imagesearch()
            if pos[0] != -1:
                print(i, "at x:", pos[0], "y:", pos[1])
                num_pos.append(pos)
            else:
                break
        for pos in num_pos:
            pyautogui.click(x=pos[0]+25, y=pos[1]+25) #add 25 to compensate for finding at top left
    pyautogui.moveTo(1,1) #moves to corner as to not obstruct things
    num_pos = [] #reset array so it's not clicking old stuff
    #this only works up to 20 but that's already 100 percentile, at that point just click random things I guess