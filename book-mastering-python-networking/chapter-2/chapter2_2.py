#!/usr/bin/env python

import getpass
import pexpect
import sys

devices = {'iosv-1' : {'prompt': 'R1', 'ip' : '10.10.20.171'},
           'iosv-2' : {'prompt': 'R2', 'ip' : '10.10.20.172'}}


commands = ['term length 0', 'show version', 'show run']

username = input('Username:')
password = getpass.getpass('Password: ')

#Start the Loop for devices
for device in devices.keys():
    outputFileName = device + '_output.txt'
    device_prompt = devices[device]['prompt']
    child = pexpect.spawn('telnet ' + devices[device]['ip'])
    #child.logfile = sys.stdout.buffer 
   
    #Authentication
    child.expect('Username:')
    child.sendline(username)
    child.expect('Password:')
    child.sendline(password)
    child.expect(device_prompt +'>')

    #Enable mode
    child.sendline('enable')
    child.expect('Password:')
    child.sendline(password)
    child.expect(device_prompt +'#')
   
    #Starts the Loop for commands and write to output file
    with open(outputFileName, 'wb') as f:
        for command in commands:
            child.sendline(command)
            child.expect(device_prompt +'#')
            f.write(child.before)
    
    #Close the connection
    child.sendline('exit')



