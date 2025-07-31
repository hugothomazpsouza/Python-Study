# Python Virtual Environment & Pexpect for Network Automation

## 📦 Python Virtual Environment

When working with Python virtual environments, we are creating *isolated environments* to separate package installations for different projects. This prevents conflicts between dependencies and avoids breaking other environments.

### ✅ Creating a Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### ❌ Deactivating the Virtual Environment

```bash
(.venv)$ deactivate
```

For more information:\
👉 [Python Packaging: Installing with pip and virtual environments](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/)

---

## 🐍 Python Pexpect Library

The `pexpect` library is useful when starting out with Python for network automation. It simulates human-like interactions with terminal-based programs, such as routers or switches.

### Example:

- Connect to a router
- Expect the prompt: `Username:`
- Send the username
- Expect the prompt: `Password:`
- Send the password
- Then proceed with commands like `enable`, `configure terminal`, etc.

This line-by-line interaction mimics what a human would do manually.

---

## 🔧 Pexpect Installation

To install `pexpect` in your virtual environment:

```bash
(.venv)$ pip install pexpect
```

> **Note:** `pip` is the standard Python package manager used to install and update packages within a virtual environment.

---

## 🛠️ Key Pexpect Methods

### `expect()`

This method waits for specific output from the terminal (e.g., a prompt or string). When the expected text (or pattern) appears, the script continues.

**Example:**

```python
child.expect("Username:")
```

Means: *"Wait until the program prints 'Username:'"*

**Tips:**

- To match upper or lowercase: `child.expect('[Uu]sername')`
- To match one of several options: `child.expect(['Username', 'username'])`

### `sendline()`

This method sends a string plus an ENTER keystroke to the terminal.

**Example:**

```python
child.sendline("admin")
```

Sends the string `admin` and presses ENTER.

---

## 🔍 Understanding `child.before` and `child.after`

After calling `child.expect()`, two properties are often useful:

- `child.before`: Contains everything printed **before** the matched pattern.
- `child.after`: Contains the **matched pattern** itself.

### 💡 Golden Tip:

Use `child.before` to get the output before the prompt, and `child.after` to confirm what was matched.

### 📘 Example:

```python
import pexpect
import sys

devices = {'iosv-1': {'prompt': 'R1', 'ip': '10.10.20.171'}}

username = 'cisco'
password = 'cisco'

for device in devices:
    device_prompt = devices[device]['prompt']
    child = pexpect.spawn('telnet ' + devices[device]['ip'])
    child.expect('Username:')
    child.sendline(username)
    child.expect('Password:')
    child.sendline(password)
    child.expect(device_prompt + '>')
    child.sendline('enable')
    child.expect('Password:')
    child.sendline(password)
    child.expect(device_prompt + '#')
    child.sendline('show version | i V')
    child.expect(device_prompt + '#')
    print(child.before)
    child.sendline('exit')
```

### 📸 Output Example:

```bash
b'show version | i V\r\nCisco IOS Software ...'
```

---

## ❓ What does `b'...'` mean in Python?

When you see `b'some text'`, it means the string is in **byte format** — not a regular text string.

### 📌 Why does Pexpect return byte strings?

Because it reads directly from the terminal, which returns data as raw **bytes**.

### 🔀 How to convert to normal string?

Use `.decode()`:

```python
output = child.before.decode()
print(output)
```

| Example            | Type    | Meaning                           |
| ------------------ | ------- | --------------------------------- |
| `'text'`           | `str`   | Standard text string              |
| `b'text'`          | `bytes` | Byte string (raw binary)          |
| `b'text'.decode()` | `str`   | Converts bytes to readable string |

---

## ⏱️ Controlling Timeouts

If your connection is slow or fast, you can set a custom timeout for `expect()`:

```python
child.expect('Username:', timeout=5)
```

---

## 👨‍💻 Take Control of the Session with `interact()`

If you want to run some commands automatically and then **take over manually**, use `child.interact()`:

```python
child.sendline('show ip int brief')
child.expect('R1#')
print(child.before.decode())
child.interact()  # You now control the session manually
```

---

## 📁 Logging the Session

To log all session activity to a file:

```python
child.logfile = open('debug', 'wb')
```

Or to print all interaction to the terminal in real time:

```python
import sys
child.logfile = sys.stdout.buffer
```

---

## 🔐 SSH with `pxssh`

`pexpect` has a subclass called `pxssh`, used for SSH sessions. It works similarly to Telnet, with some improvements.

```python
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
```

### ℹ️ `auto_prompt_reset=False`

- Tells `pxssh` **not** to try to change the prompt (e.g., `export PS1`) — important for routers/switches.
- Useful for devices with known prompts like `R1>` or `R1#`.

---

## 📘 Full Script Example: Telnet Automation to Cisco Devices

```python
#!/usr/bin/env python

import getpass
import pexpect
import sys

devices = {
    'iosv-1': {'prompt': 'R1', 'ip': '10.10.20.171'},
    'iosv-2': {'prompt': 'R2', 'ip': '10.10.20.172'}
}

commands = ['term length 0', 'show version', 'show run']

username = input('Username: ')
password = getpass.getpass('Password: ')

for device in devices:
    outputFileName = device + '_output.txt'
    device_prompt = devices[device]['prompt']
    child = pexpect.spawn('telnet ' + devices[device]['ip'])
    child.logfile = sys.stdout.buffer

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
```

### 🔍 What this script does:

1. Prompts for username and password.
2. Loops over the device list.
3. Connects via Telnet.
4. Logs in and enters enable mode.
5. Executes a list of commands.
6. Saves output to `<device>_output.txt`.
7. Closes the connection.

### 🧪 Commands Used:

```python
['term length 0', 'show version', 'show run']
```

- `term length 0`: Disables `--More--` paging.
- `show version`: Shows OS and version info.
- `show run`: Shows full device configuration.

### 📀 Output Files:

- `iosv-1_output.txt`
- `iosv-2_output.txt`

### 📦 Required Libraries:

- `pexpect`: Terminal automation
- `getpass`: Secure password input
- `sys`: Log to terminal


