#!/usr/bin/env python3

# Script: 		    OPS 401 Challenge 02
# Author: 		    Lilian Mburu
# Last Revision: 	April 13th 2024
# Purpose: 		    Uptime Sensor Tool:  script that checks systems are responding.

import subprocess, time


retries = 0
status = ''
address = '8.8.8.8'

# Transmit a single ICMP (ping) packet to a specific IP every two seconds.
def validate_sleep(retries):
    if retries < 3:
        print(f'Sleeping for 2 seconds\n')
        time.sleep(2)
        uptime(retries)
    
# check ping request response
def uptime(retries):
    retries += 1
    print(f'Attempt number: {retries}')
    response = subprocess.call(['ping', '-c', '3', address])

    # For every ICMP transmission attempted, print the status variable along 
    # with a comprehensive timestamp and destination IP tested.
    print("DateTime: ", time.strftime("%a, %b %d %Y %H:%M:%S"))
    print("IP Address: ", address)
    
# Evaluate the response as either success or failure.
    if response == 0:
        # Assign success or failure to a status variable.
        status ='success'
        print("Status: ", status)
        
        print(retries)
        validate_sleep(retries)
    else: 
        status = 'failure'
        print(status)

    
uptime(retries)


