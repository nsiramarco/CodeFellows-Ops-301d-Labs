#!/usr/bin/env python3

# Import libraries

import os

# Script Name:                  Python File Handling
# Author:                       NATASHA SIRAMARCO
# Date of latest revision:      06/13/2023
# Purpose:                      Using file handling commands, create a Python script that creates a new .txt file, 
#                               appends three lines, prints to the screen the first line, then deletes the .txt file.

# Declaration of variables


# Declaration of functions

# Main
# File path
Ch10_file = "script_ch10.txt"

# Text file and appending three lines
with open(Ch10_file, "w") as file:
    file.write("Hello World!\n")
    file.write("This is my script\n")
    file.write("Goodbye World!\n")

# The first line
with open(Ch10_file, "r") as file:
    first_line = file.readline()
    print("The first line:", first_line)

# Deleting the .txt file
os.remove(Ch10_file)
print("The file is deleted:", Ch10_file)

# End

