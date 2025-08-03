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

commands = ['show ip int brief | in administratively down']

for device in devices:
    outputFileName = device + '_output.txt'
    device_prompt = devices[device]['prompt']
    child = pexpect.spawn('telnet ' + devices[device]['ip'])
    #child.logfile = sys.stdout.buffer #- Uncomment it if you want debug the script

    child.expect('Username:')
    child.sendline(username)
    child.expect('Password:')
    child.sendline(password)
    child.expect(device_prompt + '>')

    child.sendline('enable')
    child.expect('Password:')
    child.sendline(password)
    child.expect(device_prompt + '#')

    with open(outputFileName, 'wb') as f:
        for command in commands:
            child.sendline(command)
            child.expect(device_prompt + '#')
            f.write(child.before)

    child.sendline('exit')

