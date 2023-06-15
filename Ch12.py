#!/usr/bin/env python3
import os
import requests

# Script Name:                  Python Requests Library
# Author:                       NATASHA SIRAMARCO
# Date of latest revision:      06/15/2023
# Purpose:                      Create a Python script that performs the following:
#                               Prompt the user to type a string input as the variable for your destination URL.
#                               Prompt the user to select a HTTP Method of the following options:
#                                   GET
#                                   POST
#                                   PUT
#                                   DELETE
#                                   HEAD
#                                   PATCH
#                                   OPTIONS
#                               Print to the screen the entire request your script is about to send. Ask the user to confirm before proceeding
#                               Using the requests library, perform a request against the destination URL with the HTTP Method selected by the user.
#                               For the given header, translate the codes into plain terms that print to the screen; for example, a 404 error should 
#                                   print Site not found to the terminal instead of 404.
#                               For the given URL, print response header information to the screen.


# Main
# Destination URL
url = input("Enter URL destination: ")
http_method = input("Select an HTTP Method: (GET, POST, PUT, DELETE, HEAD, PATCH, OPTIONS): ")

# Print request and confirmation
print(f"Sending {http_method} request to {url}")
confirmation = input("Press 'y' to confirm: ")
if confirmation.lower() != 'y':
    print("Request cancelled")
else:
    response = requests.request(http_method, url)

    print("\nResponse Header Information: ")
    for key, value in response.headers.items():
        print(f"{key}: {value}")
# Translation Status
    status_map = {
        200: 'Good',
        201: 'Created',
        204: 'No Content',
        400: 'Bad Request',
        401: 'Unauthorized',
        403: 'Forbidden',
        404: 'Not Found',
        405: 'Method Not Allowed',
        500: 'Internal Server Error'
    }
    status_code = response.status_code
    status_text = status_map.get(status_code, 'Unknown Status')
print(f"\nResponse Status: {status_text}")


# End 