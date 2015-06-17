---
title: "Project 2"
published: true
morea_id: project2
morea_type: experience
morea_sort_order: 7
morea_summary: "Image Manipulation"
morea_labels:
 - due 6/25
---

# Project 2: Image ManipulationIn this project you will have the opportunity to programmatically manipulate png image files with python.First, download [project2.zip](project2.zip) and unzip it. You should see the following files:
  * **Test images**: `arch.png`, `hmcOlinSmall.png`, `in.png`, `out.png`, `spam.png`, `trees.png`  * Programs:
     * `image_fun.py`: where you will write your project code
     * `png.py`: library to work with png files **DO NOT MODIFY**
     * `png_helper.py`: helper functions to manipulate png files **DO NOT MODIFY**
     
**Rename the folder** so that it is `project2_uLogin` rather than just `project2`. If you are working with a partner, make sure both uLogins are listed.

Next, try running the code: `python image_fun.py`. **Make sure to run with python, NOT python3.** If successful, when you `ls` you should see a new file, `out2.png`. Open `out2.png` and `out.png` to make sure they look the same.

## Understanding `invert`

Read over the `invert` function in `image_fun.py` to see how it works. At the bottom of the file, change the call to invert to use the `in.png` image: <img src="in.png">. Once inverted, it should look like: <img src="out.png">. Similarly:

<img src="hmcOlinSmall.png" width="200"> <img src="outOlin.png" width="200">

The `invert` function modifies an image to create its negative. That is, all color values are 255 minus their original value. Especially note the use of list comprehension in `invert`, which iterates over every pixel in the image and calls `change(rgb values)`. It's easiest to also write greyscale and binarize in the same format: a main function that accepts user input and contains a list comprehension that calls a helper function on each pixel. 

## Playing with Pixels

### grayscale

Write a function called `grayscale` that modifies an image to make it grayscale. For this, you'll want to do something similar to `invert`, except that your new change function will calculate the [luminance](http://en.wikipedia.org/wiki/Luminance_(relative)) of the pixel. For example:

<img src="spamin.png" width="200"> <img src="spamout.png" width="200">

<!--As Wikipedia calculates it, luminance is 21% red, 72% green, and 7% blue. Intuitively, this makes sense because if you think of standard red, green, and blue, green is the lightest and thus has highest positive impact luminance, while blue is darker and has a lower value for luminance. -->

Since luminance is an indication of how white/black a pixel is, having your helper function return a list of RGB values in greyscale is easy -- just return the same value in each of the three color channels!

***Hints:***

* Getting an **OverflowError: unsigned byte integer is greater than maximum**? This might be because your luminance calculation results in RGB values higher than 255. Make sure that all of your percentages add up to 1.
* Getting a **filename is not defined** error? Make sure you have single quotes around the image name when you call it in Python shell, the image is in the same folder as your python script, and permissions on your image are correct. 

### binarize

Write a function called `binarize( thresh )`, which binarizes an image (makes it black and white) with a threshold `thresh` given by the user. This threshold is a brightness value between 0 and 255 - if a pixel is greater than the threshold value, then it should turn white, and if its less than the threshold value, then it should turn black. So, a threshold value of 0 means that your photo will turn white and a threshold of 255 means your photo will turn black. For example:

<img src="spamin.png" width="200"> <img src="binaryspam.png" width="200">

## Geometric Transformations

### flipVert

Write a function called `flipVert`, which flips the image on its horizontal axis (the bottom is on the top and the top is on the bottom). For example:

<img src="in.png"> <img src="out2.png">

You will use the same basic structure as the earlier problems--one main function that opens the file and calls the helper function in a list comprehension.

***Hints:***

* In `flipVert`, you'll want to iterate over only the rows instead of the pixels in `Im_pix` and reverse their order. 
* If `L` is a list, then `L[::-1]` is the reverse of that list. 

### flipHoriz

Write a function `flipHoriz` that flips the image on its vertical axis. This should work in the same way as `flipVert` but flip in the horizontal direction. For example:

<!--<img src="spamin.png" width="200">--> <img src="fliphspam.png" width="200">

Instead of reordering the rows, you want to consider how the pixels in the rows reorder when an image is flipped horizontally. Note: flipping `in.png` horizontally has no effect because it is symmetric about the vertical axis.

## Submission

Once you’re satisfied that your programs are working correctly, zip it for submission:

  * `cd ..`
  * `zip project2_uLogin.zip project2_uLogin/*`

----
*Adapted from [Harvey Mudd's CS 5 Fun with Images](https://www.cs.hmc.edu/twiki/bin/view/CS5/FunWithImagesGold2010).*