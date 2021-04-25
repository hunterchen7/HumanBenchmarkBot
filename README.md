# HumanBenchmarkBot
 Automation of tasks on [Human Benchmark](https://humanbenchmark.com/) using python, just for fun
 
 Here's what I've got working:
 - chimp test
 - typing test
 - aim trainer
 - reaction timer
 - verbal memory
 
 Everything else is either a work in progress or I haven't started.
 Why did I make this? I was bored and thought this would be something fun to do.
 It's entirely pointless and meaningless but I thought it'd be a bit of a challenge and it would be fun so here I am..
 
 To use, run the scripts when you're on the respective tests, I suppose I could even automate the entire thing at some point as well...
 
 Here's how the working stuff currently works:
 - Chimp test: looks for the boxes with numbers on screen with the screen_search library and stores their locations in an array, pyautogui then clicks the locations in order.
 - Typing test: uses Tesseract to recognize text in the box and then types it with pyautogui.write().
 - Aim trainer: searches for the target on screen (also screen_search) and clicks it, to increase performance the target used here is just a small portion of the real target.
 - Reaction time: waits for a certain pixel to turn green and clicks, if it's blue it'll wait 2 seconds before clicking so the user can see how long the computer took.
 - Verbal memory: Sees a word, checks if it's in the list of words it's seen, if not then click new and add to the list, click seen and add to the list otherwise.

Well how does it perform? Here are the tests available:

![bot benchmark](https://user-images.githubusercontent.com/34012681/115993091-6c8c3880-a58e-11eb-830e-a850b1e7f8f1.PNG)

Quite admirable, as expected.

I believe reaction time isn't 100 percentile due to a bottleneck with loading the color of the pixel, either from the snapshot or getting the actual value. It may be worth experimenting with libraries other than Pillow and seeing if they're faster (such as PyWin32). And AimTrainer is slower the larger the image is, so I can probably speed it up by making the area that it searches smaller, and the image that it searches for smaller.

