import cv2
import pytesseract
import pyautogui
from screen_search import *

topLeft = Search("images/top_left_corner.png").imagesearch()
left = topLeft[0] 
top = topLeft[1]
bottomRight = Search("images/bottom_right_corner.png").imagesearch()
right = bottomRight[0] + 20 #takes location of top left so add 20
bottom = bottomRight[1] + 20 #same deald

pyautogui.screenshot(region=(left, top, right - left, bottom - top)).save("images/text.png")
img = cv2.imread("images/text.png")

text = pytesseract.image_to_string(img)
fixed = ""

#print(list(text))

for i in text:
    if i == "|": #detects I as | for whatever reason
        fixed += "I"
    elif i == '\n': # new lines become spaces
        fixed += ' '
    else:
        fixed += i

#text can still contain consecutive spaces so that needs to be fixed
fixed_l = list(fixed)
i = 0
while i <= len(fixed_l) - 1:
    if fixed_l[i] == ' ' and fixed_l[i-1] == ' ':
        del fixed_l[i]
    i += 1

fixed = ''.join(fixed_l)

print(topLeft, bottomRight)
#print(text)
print(fixed)

pyautogui.click(x=left+50,y=top+50) #return focus to text box

pyautogui.write(fixed) 

