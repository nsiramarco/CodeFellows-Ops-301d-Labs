#!/bin/bash

# Script Name:                  Ops Challenge: File Permissions
# Author:                       NATASHA SIRAMARCO
# Date of latest revision:      06/01/2023
# Purpose:                      Create a new bash script that performs the following:
#                               Prompts user for input directory path.
#                               Prompts user for input permissions number (e.g. 777 to perform a chmod 777)
#                               Navigates to the directory input by the user and changes all files inside it to the input setting.
#                               Prints to the screen the directory contents and the new permissions settings of everything in the directory.

# Declaration of variables

# Declaration of functions


# Main
# user for input directory path and the permissions number
read -p "Input directory path: " Directory_Path
read -p "Input permissions number (e.g., 777 to perform chmod 777): " permissions

# Navigate to directory
cd "$Directory_Path"

# Change permissions of all files in the directory
chmod -R "$permissions" *

# Print directory contents and new permissions settings
echo "Directory Contents:"
ls -l

# End