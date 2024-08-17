# Vulnerability Scanner

A simple Python script to perform basic vulnerability scanning using `nmap`, parse the results, and generate a report. This script is intended for educational purposes and to demonstrate how to integrate `nmap` with Python for automated vulnerability assessments.

## Features

- Run `nmap` scans on a target IP or hostname.
- Parse the scan results to identify potential vulnerabilities.
- Write the results to a text file in the same directory.

## Prerequisites

1. **Python**: Ensure Python 3.x is installed on your system.
2. **nmap**: Install `nmap` to perform the vulnerability scans. Installation instructions can be found on the [nmap official website](https://nmap.org/book/install.html).

   To install `nmap` on Debian-based systems (e.g., Ubuntu), you can use:

   ```bash
   sudo apt-get install nmap
   ```

## Usage

1. **Clone the repository:**
   ```bash
   git clone https://github.com/JiruGutema/Python-Valnerablity-Scanner.git
   ```
2. **Navigate to the project directory:**
   ```bash
   cd Python-Valnerablity-Scanner.git
   ```
3. **Run the script:**
   ```bash
   python Scanner.py <target_ip_or_hostname>
   ```
   Replace `<target_ip_or_hostname>` with the IP address or hostname of the target system.

## Example

```bash
python Scanner.py 192.168.1.100
```

## Output

The script will generate a text file named `vulnerability_report.txt` in the same directory. The report will contain details about the identified vulnerabilities.

## Disclaimer

This script is provided for educational purposes only. It may not detect all vulnerabilities, and its results should not be considered definitive. Always consult official security documentation and best practices for thorough vulnerability assessments.

<h1 style="color:red">Remember!</h1>
 <p style="color:green; font-family:monospace;font-weight: bold"> This Project is on-going Project as of August 2024! <br>
     More features are to be added later </p>
<footer style="color:dodgerblue; 
font-weight:bold;font-size:24px; 
text-align:center; 
border:2px solid gold;
width:20%; 
margin:auto;
border-radius:8px">Jiren</footer>

