# Python Networking Exercises

## Exercise 1: Telnet to multiple Cisco IOS devices and collect administratively down interfaces

🧠 **Challenge Exercise (No Answer Provided)**

### 💡 Scenario:
You are a junior network automation engineer. Your task is to write a Python script that connects via Telnet to multiple Cisco IOS devices and collects only the interface status of all interfaces that are administratively down.

### ✅ Requirements:
- Use the same device structure as in your current script (device name, IP, prompt).
- Ask for username and password securely.
- Use `pexpect` to:
  - Telnet into each device
  - Log in
  - Enter enable mode
  - Run the command: `show ip interface brief`
  - Parse the output (filtering only lines where the **Status** is **"administratively down"**)
  - Save the filtered output in a file named `<device_name>_down_interfaces.txt`

### 🧱 Constraints:
- You must use `pexpect`, not `Netmiko` or `Paramiko`.
- You should only write interfaces that are administratively down.
- Output file content should be clean and readable (no prompts or extra CLI characters).

---

## 🧪 Exercise 2:  Compare Running Configs Across Devices

🧠 **Challenge Exercise (No Answer Provided)**

### 💡 Scenario:
You’re now a mid-level automation engineer. The team has provided a **golden configuration file** (`golden_config.txt`) that all routers should match. Your task is to automate the retrieval of each device's running config and compare it to the golden baseline to detect configuration drift.

### ✅ Objectives:
- Connect to multiple Cisco routers using **Telnet** and `pexpect`.
- Authenticate and enter **enable mode**.
- Run the command: `show running-config`.
- Compare the output against a local `golden_config.txt` file.
- Save the **differences** to a per-device file like: `iosv-1_config_diff.txt`.
- Print a summary of match/diff status for all devices.

### 🧱 Constraints:
- Use `pexpect`, not Netmiko/Paramiko.
- Telnet only.
- Gracefully handle timeout or authentication errors.
- Ignore dynamic config lines like timestamps or uptime (if needed).



