#!/usr/bin/env python3
import os


# Script Name:                  Directory Creation
# Author:                       NATASHA SIRAMARCO
# Date of latest revision:      06/08/2023
# Purpose:                      Create a Python script that generates all directories, sub-directories and files for a user-provided directory path.
#                               Script must ask the user for a file path and read a user input string into a variable.
#                               Script must use the os.walk() function from the os library.
#                               Script must enclose the os.walk() function within a python function that hands it the user input file path.


for (root, dirs, files) in os.walk("/bin/python3"):
    for file in files:
        print(root + "/" + file)
         

# Main

### Pass the variable into the function here

# End 
