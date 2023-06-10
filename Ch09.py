#!/usr/bin/env python3
import os

# Script Name:                  Python Conditional Statements
# Author:                       NATASHA SIRAMARCO
# Date of latest revision:      06/10/2023
# Purpose:                      - Create if statements using these logical conditionals below. 
#                                   Each statement should print information to the screen depending on if the condition is met.
#                                   Equals: a == b
#                                   Not Equals: a != b
#                                   Less than: a < b
#                                   Less than or equal to: a <= b
#                                   Greater than: a > b
#                                   Greater than or equal to: a >= b
#                               - Create an if statement using a logical conditional of your choice 
#                                 and include elif keyword that executes when other conditions are not met.
#                               - Create an if statement that includes both elif and else to execute when both if and elif are not met.


# Declaration of variables
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

# Declaration of functions

# Main
if a == b:
    print("a is equal to b")
elif a < b:
    print("a is less than b")
else:
    print("a is greater than b")
# End