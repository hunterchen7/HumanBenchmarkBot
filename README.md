# HumanBenchmarkBot
 Automation of tasks on [Human Benchmark](https://humanbenchmark.com/) using python, just for fun. Try it for yourself if you've never done it! (Without the bot of course)
 
 Here are what my actual scores look like...
 ![image](https://user-images.githubusercontent.com/34012681/116012273-df290280-a5e6-11eb-9bee-9215af3c807e.png)

 But let's get to the bot.
 
 Here's what I've got working:
 - chimp test
 - typing test
 - aim trainer
 - reaction timer
 - verbal memory
 - visual memory
 
 Everything else is either a work in progress or I haven't started.
 Why did I make this? I was bored and thought this would be something fun to do.
 It's entirely meaningless to try and get higher scores, but I thought it'd be a bit of a fun challenge so here I am..
 
 To use, run the scripts when you're on the respective tests, I suppose I could even automate the entire thing at some point as well...
 
 Almost all of them are just infinite loops so you'll have to ctrl+alt+del and move your cursor to the edge of your screen to trigger the pyautogui fail safe in order to stop some of them. Others, you will have enough time to close the program. The Aim Trainer WILL probably open new tabs because the new tab button is similar enough to the target.
 
 Here's how the working stuff currently works:
 - Chimp test: looks for the boxes with numbers on screen with the screen_search library and stores their locations in an array, pyautogui then clicks the locations in order.
 - Typing test: uses Tesseract to recognize text in the box and then types it with pyautogui.write().
 - Aim trainer: searches for the target on screen (also screen_search) and clicks it, to increase performance the target used here is just a small portion of the real target.
 - Reaction time: waits for a certain pixel to turn green and clicks, if it's blue it'll wait 2 seconds before clicking so the user can see how long the computer took.
 - Verbal memory: Sees a word, checks if it's in the list of words it's seen, if not then click new and add to the list, click seen and add to the list otherwise.
 - Visual memory: takes a screenshot of the grid that appears, then finds where all the white squares occur then clicks them. 

Well how does it perform? Here are the tests available:
![bot benchmark 1 2](https://user-images.githubusercontent.com/34012681/116012188-5316db00-a5e6-11eb-8900-2755081f7b2d.PNG)
Quite admirable, as one would expect.

And I did look around a bit for a use policy and I couldn't find one so I'm fairly sure this is ok. And there's no leaderboard or anything so there's really no incentive to do it other than just because..

I believe reaction time isn't 100 percentile due to a bottleneck with loading the color of the pixel, either from the snapshot or getting the actual value. It may be worth experimenting with libraries other than Pillow and seeing if they're faster (such as PyWin32). And AimTrainer is slower the larger the image is, so I can probably speed it up by making the area that it searches smaller, and the image that it searches for smaller.

