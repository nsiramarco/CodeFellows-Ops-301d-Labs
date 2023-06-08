#!/usr/bin/env python3
import os


# Script Name:                  Directory Creation
# Author:                       NATASHA SIRAMARCO
# Date of latest revision:      06/08/2023
# Purpose:                      Create a Python script that generates all directories, sub-directories and files for a user-provided directory path.
#                               Script must ask the user for a file path and read a user input string into a variable.
#                               Script must use the os.walk() function from the os library.
#                               Script must enclose the os.walk() function within a python function that hands it the user input file path.


# Declaration of variables

### Read user input here into a variable

# Declaration of functions

### Declare a function here
def directory_files(testdir):
    for (root, dirs, files) in os.walk("testdir"):
         ### Add a print command here to print ==root==
        print("==root==")
        print(root)
        ### Add a print command here to print ==dirs==
        print("==dir==")
        print(dirs)
        ### Add a print command here to print ==files==
        print("==files==")
        print(files)

# Main

### Pass the variable into the function here

if __name__ == '__main__':
    path = input("Enter a directory path: ")
    directory_files(path)

# End