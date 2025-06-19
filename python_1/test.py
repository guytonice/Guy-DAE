So as now that you understood the project which is the automated suspicious login monitor, I need a small python file like an entire project files in which I need mock data because I don't have I don't I cannot extract logs because that is not authorized. So I want a mock log data and also I need the which is dot log file and then I need a python script that can find out suspicious patterns from the same IP at unusual hours and another pattern is login from a blacklisted IP right. So I should have multiple patterns like this for it for it to detect and it should detect something and show me an output that this is what is happening. So that it should be my project.
# Let's create the mock log file content and a Python script that reads it,
# detects suspicious patterns, and outputs findings.

# Step 1: Generate a mock log file content
mock_log_data = """
Jun 16 01:23:45 server sshd[1001]: Failed password for invalid user admin from 192.168.1.10 port 22 ssh2
Jun 16 01:24:01 server sshd[1002]: Failed password for invalid user guest from 192.168.1.10 port 22 ssh2
Jun 16 01:25:30 server sshd[1003]: Failed password for invalid user root from 192.168.1.10 port 22 ssh2
Jun 16 15:14:12 server sshd[1010]: Accepted password for user john from 203.0.113.5 port 22 ssh2
Jun 16 02:10:00 server sshd[1020]: Accepted password for user alice from 203.0.113.100 port 22 ssh2
Jun 16 02:15:11 server sshd[1021]: Accepted password for user alice from 203.0.113.100 port 22 ssh2
Jun 16 14:00:00 server sshd[1030]: Accepted password for user admin from 192.0.2.55 port 22 ssh2
"""

# Step 2: Save it to a .log file
log_file_path = "/mnt/data/mock_auth.log"
with open(log_file_path, "w") as f:
    f.write(mock_log_data)

# Step 3: Now create the Python script that will analyze this log file
python_script = '''
import re
from datetime import datetime

# Configuration
log_file = "mock_auth.log"
blacklisted_ips = {"203.0.113.100", "192.0.2.55"}
suspicious_hours = set(range(0, 5))  # 00:00 to 04:59

# Tracking variables
failed_attempts = {}
suspicious_logins = []

with open(log_file, "r") as file:
    for line in file:
        # Match IP and timestamp
        match = re.search(r"^(\\w+\\s+\\d+\\s+\\d+:\\d+:\\d+).*from\\s+(\\d+\\.\\d+\\.\\d+\\.\\d+)", line)
        if match:
            timestamp_str, ip = match.groups()
            log_time = datetime.strptime(timestamp_str, "%b %d %H:%M:%S")
            hour = log_time.hour

            if "Failed password" in line:
                failed_attempts[ip] = failed_attempts.get(ip, 0) + 1

            if "Accepted password" in line:
                if hour in suspicious_hours:
                    suspicious_logins.append((ip, "Unusual hour login", line.strip()))
                if ip in blacklisted_ips:
                    suspicious_logins.append((ip, "Blacklisted IP login", line.strip()))

# Output results
print("== Suspicious Login Report ==")
print("-- Failed Login Summary --")
for ip, count in failed_attempts.items():
    if count >= 3:
        print(f"[!] Multiple failed attempts from {ip}: {count} times")

print("-- Suspicious Successful Logins --")
for ip, reason, detail in suspicious_logins:
    print(f"[!] {reason} from {ip}: {detail}")
'''

script_path = "/mnt/data/login_monitor.py"
with open(script_path, "w") as f:
    f.write(python_script)

# Return the paths to the user
log_file_path, script_path



if __name__ == "__main__":
    log_file_path, script_path = main()        