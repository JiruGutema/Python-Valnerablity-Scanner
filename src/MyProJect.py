import subprocess
import os

def run_nmap_scan(target):
    try:
        # Run the nmap scan
        result = subprocess.run(['nmap', '-sV', target], capture_output=True, text=True)
        result.check_returncode()  # Raise an exception for non-zero exit codes
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error running nmap: {e}")
        return None

def parse_nmap_output(output):
    vulnerabilities = []
    
    lines = output.split('\n')
    for line in lines:
        if "open" in line:
            vulnerabilities.append(line.strip())
    
    return vulnerabilities

def write_report(vulnerabilities, filename):
    with open(filename, 'w') as file:
        if vulnerabilities:
            file.write("Detected Vulnerabilities:\n\n")
            for vuln in vulnerabilities:
                file.write(f"{vuln}\n")
        else:
            file.write("No vulnerabilities detected.\n")

def main():
    target = input("Enter the target IP or hostname: ")
    output = run_nmap_scan(target)
    
    if output:
        vulnerabilities = parse_nmap_output(output)
        report_file = os.path.join(os.getcwd(), 'vulnerability_report.txt')
        write_report(vulnerabilities, report_file)
        print(f"Report written to {report_file}")

if __name__ == "__main__":
    main()

