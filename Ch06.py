import os
import subprocess

# Script Name:                  Bash in Python
# Author:                       NATASHA SIRAMARCO
# Date of latest revision:      06/06/2023
# Purpose:                      The Python module “os” must be utilized
#                               At least three variables must be declared and referenced in Python
#                               The Python function print() must be used at least three times
#                                   Include execution of the following bash commands inside your Python script:
#                                   whoami
#                                   ip a
#                                   lshw -short
#                               
# Declaration of variables

# Declaration of functions


# Main
# Whoami
whoami = subprocess.check_output(['whoami']).decode('utf-8').strip()

# ip a
ip_a = subprocess.check_output(['ip', 'a']).decode('utf-8').strip()

# lshw -short
lshw_short = subprocess.check_output(['lshw', '-short']).decode('utf-8').strip()

# Print the results
print("Who am I:", whoami)
print()
print("IP addresses:", ip_a)
print()
print("Hardware information:", lshw_short)



# End

