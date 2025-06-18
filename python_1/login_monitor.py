
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
        match = re.search(r"^(\w+\s+\d+\s+\d+:\d+:\d+).*from\s+(\d+\.\d+\.\d+\.\d+)", line)
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
