# Python Networking Exercise Answers

This repository provides answers to practical Python networking exercises using the `pexpect` library to automate interaction with Cisco IOS devices over Telnet.

## Exercises

- [Exercise 1: Telnet to multiple Cisco IOS devices and collect administratively down interfaces](#exercise-1-telnet-to-multiple-cisco-ios-devices-and-collect-administratively-down-interfaces)

---

```python
import getpass
import pexpect
import sys

devices = {
    'rt-p001': {'prompt': 'R1', 'ip': '10.10.20.171'},
    'rt-p002': {'prompt': 'R2', 'ip': '10.10.20.172'}
}

username = input('Username: ')
password = getpass.getpass('Password: ')

commands = ['show ip int brief | in administratively down']

for device in devices:
    output_file = f'{device}_down_interfaces.txt'
    prompt = devices[device]['prompt']
    ip = devices[device]['ip']

    child = pexpect.spawn(f'telnet {ip}')

    child.expect('Username:')
    child.sendline(username)
    child.expect('Password:')
    child.sendline(password)
    child.expect(f'{prompt}>')

    child.sendline('enable')
    child.expect('Password:')
    child.sendline(password)
    child.expect(f'{prompt}#')

    with open(output_file, 'wb') as f:
        for command in commands:
            child.sendline(command)
            child.expect(f'{prompt}#')
            f.write(child.before)

    child.sendline('exit')


```


- [Exercise 2: Compare Running Configs Across Devices](#exercise2-compare-running-configs-across-devices)

```python
#!/usr/bin/env python

import difflib
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
    currentFileName = device + '_current_config.txt'
    goldenFileName = device + '_golden_config.txt'
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
   
    for command in commands:
        if command == 'show run':
            with open(currentFileName, 'wb') as f:
                child.sendline(command)
                child.expect(device_prompt + '#')
                f.write(child.before)
        else:
            child.sendline(command)
            child.expect(device_prompt + '#')

    child.sendline('exit')


    with open(currentFileName, 'r') as r:
        current_config = r.readlines()


    with open(goldenFileName, 'r') as g:
        golden_config = g.readlines()

    print(f'✅ Diff for {device}')

    diff = list(difflib.unified_diff(
        golden_config,
        current_config,
        fromfile = currentFileName,
        tofile = goldenFileName,
        lineterm = '',
        n=0   # By default, unified_diff() includes 3 lines of context around the actual changes. This sets context lines to zero.
    ))  

    #with open(diffFileName, 'w') as dfile:
    #    dfile.writelines(diff)

    for d in diff:
        print(d)

    print('--------------------------------')
```
