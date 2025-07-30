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

- You connect to a router.
- You expect the prompt: `Username:`
- You send the username.
- You expect the prompt: `Password:`
- You send the password.
- Then you proceed with commands like `enable`, `configure terminal`, and interface configurations.

This line-by-line interaction mimics what a human would do manually.

---

## 🔧 Pexpect Installation

To install `pexpect` in your virtual environment:

```bash
(.venv)$ pip install pexpect
```

> **Note:** `pip` is the standard Python package manager used to install and update packages within a virtual environment.


