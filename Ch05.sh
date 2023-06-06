#!/bin/bash

# Script Name:                  Clearing Logs
# Author:                       NATASHA SIRAMARCO
# Date of latest revision:      6/05/2023
# Purpose:                      Write a bash script that performs the following tasks:
#                               Print to the screen the file size of the log files before compression
#                               Compress the contents of the log files listed below to a backup directory
#                               /var/log/syslog
#                               /var/log/wtmp
#                               The file name should contain a time stamp with the following format -YYYYMMDDHHMMSS
#                               Example: /var/log/backups/syslog-20220928081457.zip
#                               Clear the contents of the log file
#                               Print to screen the file size of the compressed file
#                               Compare the size of the compressed files to the size of the original log files

# Declaration of variables

# Declaration of functions


# Main
# Print to the screen the file size
echo "File Size and Name:"
stat -c '%s' /var/log/syslog /var/log/wtmp

echo 
# Compress Files into Backup Directory and TimeStamp
echo 
zip -r Backup-Directory$(date +"%Y%m%d%H%M%S").zip /var/log/syslog /var/log/wtmp
echo "Backup has been Created..."
echo 

# Print compressed file sizes
echo "Compressed File Size:"
gzip -l Backup-Directory$(date +"%Y%m%d%H%M%S").zip
echo

# Clear File Content
sudo truncate -s 0 /var/log/syslog /var/log/wtmp

# Compare sizes
echo "Comparison:"
du -h /var/log/syslog /var/log/wtmp
du -h Backup-Directory$(date +"%Y%m%d%H%M%S").zip
echo 




# End