# HumanBenchmarkBot
 automation of tasks on human benchmarks using python, just for fun
 
 Here's what I've got working:
 - chimp test
 - typing test
 - aim trainer
 
 Everything else is either a work in progress or I haven't started.
 Why did I make this? I was bored and thought this would be something fun to do.
 It's entirely pointless and meaningless but I thought it'd be a bit of a challenge and it would be fun so here I am.
 
 To use, run the scripts when you're on the respective tests, I suppose I could even automate this at some point as well...
 
 - The chimp test looks for the boxes with numbers on screen and stores their locations in an array, pyautogui then clicks the locations in order.
 - The typing test uses Tesseract to recognize text in the box and then types it with pyautogui.write(), 0.04s delay so it types at 255 WPM.
 - The aim trainer searches for the target on screen and clicks it, to increase performance the target used here is just a small portion of the real target.
