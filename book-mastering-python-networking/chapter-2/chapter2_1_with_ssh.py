from pexpect import pxssh
import sys

child = pxssh.pxssh()

child.login('10.10.20.175', 'cisco', 'cisco', auto_prompt_reset=False)

child.logfile = sys.stdout.buffer

child.expect('R1>')
child.sendline('enable')
child.expect('R1#')

child.sendline('show ip int brief')
child.expect('R1#')

print(child.before.decode())
child.logout()
