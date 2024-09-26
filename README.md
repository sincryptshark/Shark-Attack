
# 🦈 Shark Attack - Advanced Hacking Toolkit

**Shark Attack** is a modular and advanced penetration testing toolkit designed to assist ethical hackers and cybersecurity professionals in performing in-depth network reconnaissance, vulnerability detection, exploitation, and post-exploitation activities.

This toolkit offers a wide range of tools that automate and simplify various stages of penetration testing, including network scanning, SQL injection detection, XSS vulnerability checking, privilege escalation identification, and more.

---

## 🚀 Features

- **🖧 Advanced Network Scanning**: Discover open ports, services, and potential vulnerabilities on your target.
- **🔍 Reconnaissance Tools**: Perform Whois lookups, DNS enumeration, and other domain information gathering tasks.
- **🛡️ SQL Injection Detection**: Test web applications for SQL injection vulnerabilities using predefined payloads.
- **🖥️ XSS Detection**: Detect Cross-Site Scripting (XSS) vulnerabilities in web applications.
- **⚔️ Exploitation Module**: Execute reverse shells or use custom exploits to compromise the target.
- **🕵️‍♂️ Privilege Escalation**: Identify potential privilege escalation vulnerabilities on compromised machines.
- **📊 Reporting**: Automatically generate detailed reports for documentation and analysis.
- **👾 Post-Exploitation**: Maintain access and persistence with tools like reverse shells.

---

## 📦 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/shark-attack.git
   cd shark-attack
   ```

2. Install the necessary dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## 🔧 Usage

Run the main **`shark_attack.py`** script with the following options to perform different penetration testing tasks. Each flag corresponds to a specific feature of the toolkit.

```bash
python3 shark_attack.py [OPTIONS]
```

### 🖧 Network Scanning
- **Flag**: `--scan`
- **Description**: Performs an advanced network scan to discover open ports, services, and identify potential vulnerabilities.
- **Usage**:
   ```bash
   python3 shark_attack.py --scan
   ```

### 🔍 Reconnaissance Tools
- **Flag**: `--recon`
- **Description**: Runs reconnaissance tools like Whois and DNS enumeration to gather domain information.
- **Usage**:
   ```bash
   python3 shark_attack.py --recon
   ```

### 🛡️ SQL Injection Detection
- **Flag**: `--sql`
- **Description**: Tests for SQL Injection vulnerabilities in web applications by sending malicious payloads.
- **Usage**:
   ```bash
   python3 shark_attack.py --sql
   ```

### 🖥️ XSS Vulnerability Detection
- **Flag**: `--xss`
- **Description**: Detects Cross-Site Scripting vulnerabilities by injecting JavaScript payloads into forms or URLs.
- **Usage**:
   ```bash
   python3 shark_attack.py --xss
   ```

### ⚔️ Exploitation Module
- **Flag**: `--exploit`
- **Description**: Runs the exploitation module to exploit discovered vulnerabilities. Includes reverse shells and other custom exploit payloads.
- **Usage**:
   ```bash
   python3 shark_attack.py --exploit
   ```

### 🕵️‍♂️ Privilege Escalation
- **Flag**: `--priv-esc`
- **Description**: Scans the target system for privilege escalation opportunities by identifying misconfigured SUID binaries or services.
- **Usage**:
   ```bash
   python3 shark_attack.py --priv-esc
   ```

### 👾 Post-Exploitation
- **Flag**: `--post-exploit`
- **Description**: Runs post-exploitation tools like reverse shells and persistence mechanisms to maintain access on the compromised target.
- **Usage**:
   ```bash
   python3 shark_attack.py --post-exploit
   ```

### 📊 Generate Reports
- **Flag**: `--report`
- **Description**: Generates a detailed report of the performed tests and detected vulnerabilities for analysis and documentation.
- **Usage**:
   ```bash
   python3 shark_attack.py --report
   ```

---

## 📖 Example Usage

Here’s how you can use multiple options to perform different tasks:

### 1. Perform a Network Scan:
```bash
python3 shark_attack.py --scan
```

### 2. Test for SQL Injection Vulnerabilities:
```bash
python3 shark_attack.py --sql
```

### 3. Run Exploitation Module:
```bash
python3 shark_attack.py --exploit
```

### 4. Run Privilege Escalation Checks:
```bash
python3 shark_attack.py --priv-esc
```

---

## 🚨 Disclaimer
This toolkit is intended for **educational** and **legal penetration testing** purposes only. Use it on systems that you have explicit permission to test. Misuse of this toolkit can lead to legal consequences, and the author is not responsible for any illegal use or damage caused by this toolkit.

---

## 💻 License
This project is licensed under the MIT License - see the LICENSE file for details.
