import psutil

def monitor_cpu_usage():
    print(f"CPU Usage: {psutil.cpu_percent(interval=1)}%")

if __name__ == "__main__":
    monitor_cpu_usage()
