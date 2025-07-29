import pexpect
import sys


def show_int(name, ip, user, password):
    # Spawn the telnet session
    child = pexpect.spawn(f'telnet {ip}', encoding='utf-8')

    # Enable real-time logging to terminal
    #child.logfile = sys.stdout.buffer

    # Login process
    child.expect('Username:')
    child.sendline(user)

    child.expect('Password:')
    child.sendline(password)

    # Wait for the router prompt (R1>)
    child.expect(f'{name}>')

    # Enter privileged exec mode
    child.sendline('enable')
    child.expect('Password:')
    child.sendline(password)

    # Wait for the privileged prompt (R1#)
    child.expect(f'{name}#')

    # Run the show version command
    child.sendline('show ip int brief')

    # Wait for the command to complete and the prompt to return
    child.expect(f'{name}#')

    # Print the command output
    return child.before
    #output = child.before.decode()
    #print("\nCommand Output:\n", output)

    # Exit session
    child.sendline('exit')


devices = [
   {'name' : 'R1', 'ip' : '10.10.20.171', 'user' : 'cisco', 'password' : 'cisco'},
   {'name' : 'R2', 'ip' : '10.10.20.172', 'user' : 'cisco', 'password' : 'cisco'}
]

for device in devices:
    output = show_int(**device)
    print(output)
