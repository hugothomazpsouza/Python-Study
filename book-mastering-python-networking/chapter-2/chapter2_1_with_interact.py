import pexpect
import sys

devices = {'iosv-1' : {'prompt': 'R1', 'ip' : '10.10.20.171'}}


username = 'cisco'
password = 'cisco'

for device in devices.keys():
    device_prompt = devices[device]['prompt']
    child = pexpect.spawn('telnet ' + devices[device]['ip'])
    #child.logfile = sys.stdout.buffer ### It is a debug to print each step of the script
    child.expect('Username:')
    child.sendline(username)
    child.expect('Password:')
    child.sendline(password)
    child.expect(device_prompt +'>')
    child.sendline('enable')
    child.expect('Password:')
    child.sendline(password)
    child.expect(device_prompt +'#')
    child.sendline('show ip int brief')
    child.expect(device_prompt +'#')
    print(child.before.decode())
    child.interact()
