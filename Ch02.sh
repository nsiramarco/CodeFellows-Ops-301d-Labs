#!/bin/bash

# Script Name:                  Ops Challenge: Append; Date and Time
# Author:                       NATASHA SIRAMARCO
# Date of latest revision:      06/01/2023
# Purpose:                      Manipulate a variable in bash to apply today’s date to a log file. 
#                               Resource: [Shell style guide](https://google.github.io/styleguide/shellguide.html)

# Declaration of variables

# Declaration of functions


# Main
# Set the source and destination filenames
File_SystemLog="/var/log/syslog"
Create_Directory="$(date -d "$current_date" +"%B %e, %Y") File System Log"

# Copy the source file to the destination
cp "$File_SystemLog" "$Create_Directory"

# Display success message
echo "Copied $File_SystemLog and created the $Create_Directory Directory"


# End
