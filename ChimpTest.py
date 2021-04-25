from screen_search import *

num_pos = []

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