---
title: "Practice HW2: UNIX Command Overview"
published: true
morea_id: hw2
morea_type: experience
morea_sort_order: 5
morea_summary: "Practice HW: UNIX & python"
morea_labels:
 - due 5/27
---
# Practice HW2: UNIX Command Overview & Running your first Python Program

## UNIX Command Overview

For each of the following commands:

A. Briefly describe what it does in your own words. Example: 

    wget downloads files from the internet

B. Write a template of how the command is used -- indicate arguments in [brackets]. For example, a template for the wget command would look like this:

    wget [url to download]

Alternatively, the zip command to submit an assignment might look like this:

    zip [folder].zip [folder]/*

C. Take a screenshot of using the command on your terminal (please crop irrelevant parts<!--, but make sure to show your prompt so I can see it’s your computer and not someone else’s)-->. You should make sure the command works in the screen shot.

   Example for **wget**:

   <a href="wget.png"><img src="wget.png" width="500"/></a>

   The example for **remove** also needs to show the file is no longer there:

   <a href="rm.png"><img src="rm.png" width="300"/></a>

Your document should be organized by command -- for example, you should describe the ls command, give its template, and include a cropped screenshot before moving on to the next command, pwd.

**Commands:**

1. ls
1. pwd
1. cd
1. touch
1. mkdir
1. cp
1. mv
1. rm
1. ped
1. cat
1. zip    
1.  .      (not a command, use in conjunction with another command)
1. ..      (not a command, use in conjunction with another command)
1. tab     (no screenshot necessary)
1.  ↑      (no screenshot necessary)

**How to take *& crop* a Screenshot**

- Windows: [www.ehow.com/how_6801557_crop-screen-shot.html](www.ehow.com/how_6801557_crop-screen-shot.html)
- Mac: [http://www.ehow.com/how_4559274_take-edit-screen-shots-mac.html](http://www.ehow.com/how_4559274_take-edit-screen-shots-mac.html)
    - Make sure to use Command (⌘)-K rather than control-K as the article states.

## Running your first python program

In a graded WOD or project, I would give you directions like this:

1. Create a folder (`mkdir hw2_uLogin`) where you replace `uLogin` with your Drew e-mail address before the @ sign.
2. Go into this folder by typing `cd hw2_uLogin` and create a python file: `touch hello_world.py`
3. Edit the file (`ped hello_world.py`) to print "Hello, World!". *Make sure to save your file.*
4. Run your python program: `python3 hello_world.py`
5. Once you're satisfied that your program is working correctly, zip it for submission:
    - `cd ..`
    - `zip hw2_uLogin.zip hw2_uLogin/*`

## Demonstration

Once you've finished doing the WOD a single time, you can watch me do it:

{% include youtube.html id="bMbr3Xpbgzk" %}

{% include wod-warning.html %}

### Screenshot of my final UNIX terminal:

<a href="terminalA.png"><img src="terminalA.png" width="400"/></a><BR>
<a href="terminalB.png"><img src="terminalB.png" width="400"/></a><BR>
<a href="terminalC.png"><img src="terminalC.png" width="400"/></a>