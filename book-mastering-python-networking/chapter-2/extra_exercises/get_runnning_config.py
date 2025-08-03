#!/usr/bin/env python

import getpass
import pexpect
import sys


devices = {
    'rt-p001' : {'prompt' : 'R1', 'ip' : '10.10.20.171'},
    'rt-p002' : {'prompt' : 'R2', 'ip' : '10.10.20.172'}
}

username = input('Username: ')
password = getpass.getpass('Password: ')

commands = ['terminal length 0', 'show run']

for device in devices:
    outputFileName = device + '_current_config.txt'
    device_prompt = devices[device]['prompt']
    child = pexpect.spawn('telnet ' + devices[device]['ip'])
    child.logfile = sys.stdout.buffer #- Uncomment it if you want debug the script

    child.expect('Username:')
    child.sendline(username)
    child.expect('Password:')
    child.sendline(password)
    child.expect(device_prompt + '>')

    child.sendline('enable')
    child.expect('Password:')
    child.sendline(password)
    child.expect(device_prompt + '#')
   
    for command in commands:
        if command == 'show run':
            with open(outputFileName, 'wb') as f:
                child.sendline(command)
                child.expect(device_prompt + '#')
                f.write(child.before)
        else:
            child.sendline(command)
            child.expect(device_prompt + '#')

    child.sendline('exit')

