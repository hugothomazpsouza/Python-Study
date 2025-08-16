# Paramiko Library

Paramiko is a Python implementation of the SSHv2 protocol. It focuses only on SSHv2 with no Telnet support.

## ✅ Creating a Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## Installation of Paramiko

It’s pretty straightforward with Python pip. Due to the encryption used for the SSH protocol, there is a hard dependency on the `cryptography` library.

**Cryptography library installation instructions:**  
[https://cryptography.io/en/latest/installation/](https://cryptography.io/en/latest/installation/)

**Paramiko installation steps:**
```bash
pip install cryptography
pip install paramiko
```

---

## Paramiko Overview

### Example Script in Interactive mode
```python
Python 3.9.6 (default, Apr 30 2025, 02:07:17) 
[Clang 17.0.0 (clang-1700.0.13.5)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 
>>> 
>>> import paramiko
>>> import time
>>> 
>>> 
>>> 
>>> connection = paramiko.SSHClient()
>>> connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
>>> connection.connect('10.10.20.171', username='cisco', password='cisco', look_for_keys=False, allow_agent=False)
>>> 
>>> new_connection = connection.invoke_shell()
>>> output = new_connection.recv(5000)
>>> print(output)
b'\r\n\r\nR1>'
>>> 
>>> print(output.decode)
<built-in method decode of bytes object at 0x101d69ed0>
>>> print(output.decode())


R1>
>>> 
>>> 
>>> new_connection.send('enable\n')
7
>>> output = new_connection.recv(5000)
>>> print(output.decode())
enable
Password: 
>>> new_connection.send('cisco\n')
6
>>> output = new_connection.recv(5000)
>>> print(output.decode())

% Password:  timeout expired!
Password: 
R1#
>>> 
>>> 
>>> new_connection.send('show version | i V\n')
19
>>> output = new_connection.recv(5000)
>>> print(output.decode())
show version | i V
Cisco IOS Software [Dublin], Linux Software (X86_64BI_LINUX-ADVENTERPRISEK9-M), Version 17.12.1, RELEASE SOFTWARE (fc5)
256K bytes of NVRAM.
R1#
>>> 

```

## Code Walkthrough - Python interactive mode 

### 1. Import required libraries
```python
import paramiko
import time
```
- `paramiko` → allows Python to connect to devices via SSH.  
- `time` → often used for delays (e.g., `sleep`) when sending commands.

---

### 2. Create an SSH client
```python
connection = paramiko.SSHClient()
```
Creates an SSH client object called `connection`.  
Think of it like opening the SSH program, but inside Python.

---

### 3. Set host key policy
```python
connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
```
Normally SSH asks: *"Are you sure you want to continue connecting (yes/no)?"*  
This line auto-accepts the host key without asking you.

---

### 4. Connect to the router
```python
connection.connect('10.10.20.171', username='cisco', password='cisco', look_for_keys=False, allow_agent=False)
```
- Connects to `10.10.20.171`  
- Logs in with:
  - **username:** `cisco`
  - **password:** `cisco`  
- `look_for_keys=False` → don’t use SSH keys.  
- `allow_agent=False` → don’t use SSH agent.  

✅ At this point, you are connected to the router.

---

### 5. Start interactive shell session
```python
new_connection = connection.invoke_shell()
```
Starts an interactive shell session (like typing commands directly on the router console).

---

### 6. Receive initial output
```python
output = new_connection.recv(5000)
print(output)
```
- `recv(5000)` → receives up to 5000 bytes from the router.  
- Output is in raw **bytes**, e.g.:  
  ```
  b'\r\n\r\nR1>'
  ```

---

### 7. Decode output
```python
print(output.decode())
```
Converts bytes into human-readable text.  
Output shows the router prompt:
```
R1>
```

---

### 8. Enter enable mode
```python
new_connection.send('enable\n')
```
Sends the command `enable` (with Enter).  
Router now asks for an **enable password**.

---

### 9. Read router’s reply
```python
output = new_connection.recv(5000)
print(output.decode())
```
Expected reply:
```
enable
Password:
```

---

### 10. Send enable password
```python
new_connection.send('cisco\n')
```

---

### 11. Confirm privileged mode
```python
output = new_connection.recv(5000)
print(output.decode())
```
Reply may look like:
```
% Password:  timeout expired!
Password:
R1#
```
Even though it shows an error, the router accepted the password and switched to privileged exec mode (`R1#`).

---

### 12. Send show command
```python
new_connection.send('show version | i V\n')
```
Runs the command `show version | i V` → shows only lines with a capital **V**.

---

### 13. Read output
```python
output = new_connection.recv(5000)
print(output.decode())
```
Sample output:
```
Cisco IOS Software [Dublin], Linux Software ...
R1#
```

---

### 14. Close connection
```python
new_connection.close()
```
Ends the interactive shell session.  
Connection is now terminated.

### Example Script through Python file (show_vesion.py file)

```python
#!/usr/bin/env python3

import paramiko
import time
import getpass

user = input('Username: ')
passw = getpass.getpass('Password: ')

connection = paramiko.SSHClient()
connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
connection.connect('10.10.20.171', username=user, password=passw, look_for_keys=False, allow_agent=False)


new_connection = connection.invoke_shell()
output = new_connection.recv(5000)
print(output.decode())

new_connection.send('enable\n')
new_connection.send(f'{passw}\n')
time.sleep(1)
output = new_connection.recv(5000)
print(output.decode())

new_connection.send('show version | i V\n')

time.sleep(3)
output = new_connection.recv(5000)
print(output.decode())

new_connection.close()
```
### Output of the show_vesion.py file 
```
(venv) host Paramiko_library % python3 show_version.py
Username: cisco
Password: 



R1>
enable
Password: 
R1#
show version | i V
Cisco IOS Software [Dublin], Linux Software (X86_64BI_LINUX-ADVENTERPRISEK9-M), Version 17.12.1, RELEASE SOFTWARE (fc5)
256K bytes of NVRAM.
R1#
```

## Another Example: `exec_command()` Success Case and force a Failed case


```python
Python 3.9.6 (default, Apr 30 2025, 02:07:17) 
[Clang 17.0.0 (clang-1700.0.13.5)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 
>>> 
>>> import paramiko
>>> 
>>> connection = paramiko.SSHClient()                                           >>> connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())            >>> connection.connect('10.10.20.171', username='cisco', password='cisco', look_for_keys=False, allow_agent=False)
>>> 
>>> 
>>> stdin, stdout, stderr = connection.exec_command('show arp\n')
>>> stdout.read()
b'\r\n\r\n\r\nProtocol  Address          Age (min)  Hardware Addr   Type   Interface\r\nInternet  1.1.1.1                 -   aabb.cc00.0310  ARPA   Ethernet0/1\r\nInternet  1.1.1.2               113   aabb.cc00.0410  ARPA   Ethernet0/1\r\nInternet  10.10.10.100            -   aabb.cc00.0300  ARPA   Ethernet0/0'
>>> 
>>> stdin, stdout, stderr = connection.exec_command('show arp\n')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/hugothomazpinheirodesouza/python-envs/book-mastering-python-networking/chapter-2/venv/lib/python3.9/site-packages/paramiko/client.py", line 558, in exec_command
    chan = self._transport.open_session(timeout=timeout)
  File "/Users/hugothomazpinheirodesouza/python-envs/book-mastering-python-networking/chapter-2/venv/lib/python3.9/site-packages/paramiko/transport.py", line 988, in open_session
    return self.open_channel(
  File "/Users/hugothomazpinheirodesouza/python-envs/book-mastering-python-networking/chapter-2/venv/lib/python3.9/site-packages/paramiko/transport.py", line 1082, in open_channel
    raise SSHException("SSH session not active")
paramiko.ssh_exception.SSHException: SSH session not active
>>> 
```

### Code:
```python
connection.connect('192.168.2.51', username='cisco', password='cisco',
                   look_for_keys=False, allow_agent=False)
stdin, stdout, stderr = connection.exec_command('show arp\n')
stdout.read()
```

### Explanation:
1. **connection.connect(...)** → Connects to a Cisco router using SSH.
2. **exec_command('show arp\n')** → Sends the command to the router in a new SSH session channel.
3. **stdout.read()** → Reads the output of that command.

---

## Error When Running a New Command After `exec_command()`

### Example Error:
```python
>>> stdin, stdout, stderr = connection.exec_command('show arp\n')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/hugothomazpinheirodesouza/python-envs/book-mastering-python-networking/chapter-2/venv/lib/python3.9/site-packages/paramiko/client.py", line 558, in exec_command
    chan = self._transport.open_session(timeout=timeout)
  File "/Users/hugothomazpinheirodesouza/python-envs/book-mastering-python-networking/chapter-2/venv/lib/python3.9/site-packages/paramiko/transport.py", line 988, in open_session
    return self.open_channel(
  File "/Users/hugothomazpinheirodesouza/python-envs/book-mastering-python-networking/chapter-2/venv/lib/python3.9/site-packages/paramiko/transport.py", line 1082, in open_channel
    raise SSHException("SSH session not active")
paramiko.ssh_exception.SSHException: SSH session not active
>>> 
```

**Why This Happens:**
- Cisco routers often auto-close idle SSH sessions when using `exec_command()`.
- `exec_command()` creates a **temporary** session/channel.
- After it finishes, the channel closes, leaving the connection without an active channel.

**Fixes:**
1. **Reconnect Before Each Command** *(not efficient)*
```python
connection.connect(...)
stdin, stdout, stderr = connection.exec_command(...)
```
2. **Use `invoke_shell()` For Persistent Sessions** *(recommended)*
```python
shell = connection.invoke_shell()
shell.send('show version | i V\n')
time.sleep(2)
output = shell.recv(5000).decode()
print(output)
```

**Comparison Table:**
| Method         | Pros                   | Cons                                     |
|----------------|------------------------|------------------------------------------|
| `exec_command()`| Simple, 1-shot command | Session often closes after 1 use         |
| `invoke_shell()`| Persistent session     | Requires manual handling of I/O          |

---

## Understanding `stdin`, `stdout`, and `stderr` in Paramiko

When you run:
```python
stdin, stdout, stderr = ssh.exec_command('command')
```

### Streams:
- **stdin** → Standard Input (send data to the command)
- **stdout** → Standard Output (command results)
- **stderr** → Standard Error (error messages)

### Example:
```python
import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('10.10.10.1', username='admin', password='admin')

stdin, stdout, stderr = ssh.exec_command('show version')

output = stdout.read().decode()
error = stderr.read().decode()

if error:
    print("Error found:", error)
else:
    print("Command output:\n", output)

ssh.close()
```

---

## First Paramiko Program Example (from book - file name: chapter2_3.py)

```python
#!/usr/bin/env python3

import paramiko, getpass, time

devices = {'R1': {'ip': '10.10.20.171'},
           'R2': {'ip': '10.10.20.172'}
}

commands = ['show version\n', 'show run\n']

username = input('Username: ')
password = getpass.getpass('Password: ')

max_buffer = 65535

def clear_buffer(connection):
    if connection.recv_ready():
        return connection.recv(max_buffer)


# Loop through devices
for device in devices.keys():
    outputFileName = device + '_show_run_output_txt'
    connection = paramiko.SSHClient()
    connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    connection.connect(devices[device]['ip'], username=username, password=password, look_for_keys=False, allow_agent=False)
    new_connection = connection.invoke_shell()
    output = clear_buffer(new_connection)
    time.sleep(5)
    new_connection.send('enable\n')
    new_connection.send(f'{password}\n')
    new_connection.send('terminal length 0\n')
    with open(outputFileName, 'wb') as f:
        for command in commands:
            new_connection.send(command)
            time.sleep(5)
            output = clear_buffer(new_connection)
            print(output.decode())
            f.write(output)

    new_connection.close()
```

---

## About `clear_buffer()` Function

```python
def clear_buffer(connection):
    if connection.recv_ready():
        return connection.recv(max_buffer)
```

**Purpose:**  
Clears any pending output from the SSH buffer to keep the session in sync.

**Why Important:**  
When automating with `.invoke_shell()`, leftover outputs (e.g., from `enable`, `terminal length 0`, etc.) can interfere with the next command’s output.

**How It Works:**
- `connection.recv_ready()` → Checks if data is available
- `connection.recv(max_buffer)` → Reads and clears the buffer

**Example Usage:**
```python
new_connection.send("terminal length 0\n")
output = clear_buffer(new_connection)
```

**`max_buffer` Definition:**
```python
max_buffer = 65535
```

✅ Summary: Keeps automation clean by ensuring no old output is mixed with new command results.

---


# Paramiko Notes and Examples

## Paramiko for Servers

As mentioned in previous notes, Paramiko can be used to connect to Linux servers, Cisco devices, and more.  
In this example, we’ll connect to an **Ubuntu virtual machine** using **key-based authentication** (private and public key) for an SSHv2 session.

### Generating a Public and Private Key Pair
On your local machine, run:
```bash
ssh-keygen -t rsa
```
This generates:
- **Public key**: `id_rsa.pub` located in `~/.ssh`
- **Private key**: `id_rsa` located in `~/.ssh`

⚠️ **Important:** Treat your private key like your password—never share it.  

Think of the public key as your *business card* that identifies you.  
Using these keys:
- Your message is encrypted locally with your **private key**
- The remote host decrypts it using your **public key**

### Adding the Public Key to the Remote Host
From the host where the key pair was created:
```bash
cat ~/.ssh/id_rsa.pub
ssh-rsa <your public key>
```
On the remote host:
```bash
vim ~/.ssh/authorized_keys
# Paste your public key here
```

### Connecting to the Remote Host with Paramiko (Private Key Authentication)
```python
import paramiko

key = paramiko.RSAKey.from_private_key_file('/home/echou/.ssh/id_rsa')
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('192.168.199.182', username='echou', pkey=key)

stdin, stdout, stderr = client.exec_command('ls -l')
print(stdout.read())

stdin, stdout, stderr = client.exec_command('pwd')
print(stdout.read())

client.close()
```
**Note:**  
Unlike Cisco routers, which often close idle SSH sessions when using `exec_command()`, LIn a Linux server, we don’t need to create an interactive session (and always open a new connection) to execute multiple commands, as we did for Cisco routers.

**Why Private Key Authentication?**  
Because more and more network devices are adopting Linux shells with key-based authentication as a secure mechanism.



## More Paramiko Examples (Reusable Scripts - from book - file name: chapter2_4.py)

To make the Paramiko script more reusable and avoid modifying it every time we need to add or remove commands or devices—which could lead to mistakes when editing the script directly—we can make the script more flexible by using external files.

Instead of changing the script itself, users will simply update text files when they want to add or remove devices or commands.

For example, we can create a file called `commands.txt` to store the commands. In this case, the commands will apply configuration changes to adjust the logging buffer size to 30,000 bytes.

### Commands File (`commands.txt`)
```text
config t
logging buffered 30000
end
copy run start
```

The device information is stored in JSON format in a file named `devices.json. JSON was chosen because its data types can be easily converted into Python dictionary data types.

### Devices File (`devices.json`)
```json
{
    "lax-edg-r1": {
        "ip": "192.168.2.51"
    },
    "lax-edg-r2": {
        "ip": "192.168.2.52"
    }
}
```

### Loading Files in Python
```python
with open('devices.json', 'r') as f:
    devices = json.load(f)

with open('commands.txt', 'r') as f:
    commands = f.readlines()
```
- `devices.json` - we are loading the devices.json file, we are going to open the ‘devices.json’ file in read mode (‘r’), and this ‘with’ statement automatically  close the file when it’s done.

The “json.load(f)” will read the JSON file and parses it into a Python object (usually a ‘dict’ or a ‘list’)..

- `commands.txt` - iwe are going to read all lines from the commands.txt file and add it into a ‘list’. where each list element is one line of text (including the \n newline character). 

### Full Script
```python
import paramiko, getpass, time, json

with open('devices.json', 'r') as f:
    devices = json.load(f)

with open('commands.txt', 'r') as f:
    commands = f.readlines()


username = input('Username: ')
password = getpass.getpass('Password: ')

max_buffer = 65535

def clear_buffer(connection):
    if connection.recv_ready():
        return connection.recv(max_buffer)


# Loop through devices
for device in devices.keys():
    outputFileName = f'{device}_configuration_output.txt'
    connection = paramiko.SSHClient()
    connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    connection.connect(devices[device]['ip'], username=username, password=password, look_for_keys=False, allow_agent=False)
    new_connection = connection.invoke_shell()
    time.sleep(1)
    new_connection.send('enable\n')
    new_connection.send(f'{password}\n')
    output = clear_buffer(new_connection)
    time.sleep(2)
    with open(outputFileName, 'wb') as f:
        for command in commands:
            if command == 'copy run start\n':
                new_connection.send('copy run start\n')
                new_connection.send(' \n')
                time.sleep(3)
            else:
                new_connection.send(command)
                time.sleep(1)
                output = clear_buffer(new_connection)
                print(output.decode())
                f.write(output)

    new_connection.close()
```
## Output

```
Username: cisco
Password: 
enable
Password: 
R1#config t
Enter configuration commands, one per line.  End with CNTL/Z.
R1(config)#
logging buffered 30000
R1(config)#
end
R1#
copy run start
Destination filename [startup-config]?  
Building configuration...
[OK]
R1#show run | in logging buffered
logging buffered 30000
R1#
enable
Password: 
R2#config t
Enter configuration commands, one per line.  End with CNTL/Z.
R2(config)#
logging buffered 30000
R2(config)#
end
R2#
copy run start
Destination filename [startup-config]?  
Building configuration...
[OK]
R2#show run | in logging buffered
logging buffered 30000
R2#
```


---

## Key Takeaways
- Use **private key authentication** for improved security.
- Store commands and device info in **external files** to make scripts reusable and reduce risk of accidental changes.
- Linux SSH sessions are more flexible than Cisco device sessions when using `exec_command()`.











