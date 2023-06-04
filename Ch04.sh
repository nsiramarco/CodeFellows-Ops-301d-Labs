#!/bin/bash

# Script Name:                  Create Conditionals in Menu Systems
# Author:                       NATASHA SIRAMARCO
# Date of latest revision:      06/03/2023
# Purpose:                      Create a bash script that launches a menu system with the following options:
#                               Hello world (prints “Hello world!” to the screen)
#                               Ping self (pings this computer’s loopback address)
#                               IP info (print the network adapter information for this computer)
#                               Exit
#                               Next, the user input should be requested.
#                               The program should next use a conditional statement to evaluate the user’s input, then act according to what the user selected.
#                               Use a loop to bring up the menu again after the request has been executed.

# Declaration of variables

# Declaration of functions


# Main
while true; do
    echo "Make a Selection:"
    echo "1 for Hello World!"
    echo "2 for self ping"
    echo "3 for IP Information"
    echo "4 to Exit"
    read -p "Please enter your selection: " selection

    case $selection in
        1)
            echo "Hello World!!!"
            ;;
        2)
            ping -c 2 127.0.0.1
            ;;
        3)
            ip addr show
            ;;
        4)
            echo "Now Exiting..."
            echo "Complete"
            exit 0
            ;;
        *)
            echo "This is not a selection. Please try again..."
            ;;
    esac

    echo
done


# End