---
title: "Practice HW1"
published: true
morea_id: phw1
morea_type: experience
morea_sort_order: 5
morea_summary: "UNIX, Hardware, & Syntax"
morea_labels:

---
# Practice HW1: UNIX, Hardware, & Syntax

## UNIX Setup

The first step is to get access to a UNIX command line.

### Mac Users

Good news! Macs come with UNIX built-in, although you will still need to install python & a good text editor. Follow [these installation instructions](install-mac.html) and then [customized your terminal](unix-custom.html).

If the above steps don't work for your mac, you can follow the directions for Windows users, below.

### Windows Users

Windows users (and some mac users) will need to install a program called VirtualBox, which allows you to run UNIX inside of any other host operating system (OS). It's like having another computer running virtually *inside* your Windows machine. Follow [these installation instructions](install-windows.html) to setup.

## Exploring the UNIX command line

Read through the following tutorial: [http://www.davidbaumgold.com/tutorials/command-line/](http://www.davidbaumgold.com/tutorials/command-line/). Then, open your UNIX terminal and go through the following steps.

1. Let’s create a directory for this class. Type `mkdir csci117`.
1. Type `cd csci117` to move the terminal to that directory
1. Type `touch testfile.txt` to create an empty file
1. Type `ls` in the terminal. Do you see testfile.txt?
1. Type `pwd` to see what directory your terminal is in, then try to navigate your computer’s GUI (window’s explorer or mac finder) to display that directory. Do the GUI folder and terminal listing from the prior step match?
1. Let’s edit our testfile:
    - If you have [customized your terminal](unix-custom.html): `ped testfile.txt`
    - On mac: `open -a textwrangler testfile.txt`
    - On windows virtual box: `gedit testfile.txt &`
1. Type your name and save the file
1. Arrange your windows so you can see your editor and your terminal at the same time.
1. In the terminal, type `cat testfile.txt`. Is your name displayed?
1. Take a single screenshot of your desktop showing your editor and UNIX terminal window open at the same time.

## Exploring Hardware

Fill in the following blanks with: motherboard, processor, memory, hard drive:

  1. variables are stored in/on ________
  1. the ________ executes program statements
  1. when a program is not being executed, it resides in/on ________
  1. a ________ connects all the components of a computer with a bus

## Running your first python program

In a graded HW or project, I would give you directions like this:

1. Create a folder (`mkdir phw1_uLogin`) where you replace `uLogin` with your Drew e-mail address before the @ sign.
2. Go into this folder by typing `cd phw1_uLogin` and create a python file: `touch hello_world.py`
3. Edit the file (`ped hello_world.py`) to print "Hello, World!". *Make sure to save your file.*
4. Run your python program: `python3 hello_world.py`
5. Once you're satisfied that your program is working correctly, zip it for submission:
    - `cd ..`
    - `zip phw1_uLogin.zip phw1_uLogin/*`

## Demonstration

Once you've finished doing the HW a single time, you can watch me do it:

{% include youtube.html id="bMbr3Xpbgzk" %}

{% include wod-warning.html %}

### Screenshot of my final UNIX terminal:

<a href="terminalA.png"><img src="terminalA.png" width="400"/></a><BR>
<a href="terminalB.png"><img src="terminalB.png" width="400"/></a><BR>
<a href="terminalC.png"><img src="terminalC.png" width="400"/></a>

<!--## Demonstration

Once you've finished doing the HW a single time, watch me do it:

{% include youtube.html id="CIC9W_H1TjA" %}

{% include wod-warning.html %}-->

<!--## Solutions

### My Final UNIX Screenshot

<a href="screenshot.png"><img src="screenshot.png" width="400"/></a>

### Solutions to Hardware Questions

<a href="HardwareSolutions.png"><img src="HardwareSolutions.png" width="400"/></a>-->