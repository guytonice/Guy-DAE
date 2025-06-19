def find_failed_logins(log_file="/var/log/auth.log"):
    try:
        with open(log_file, "r") as file:
            for line in file:
                if "Failed password" in line:
                    print(line.strip())
    except FileNotFoundError:
        print("Log file not found or inaccessible.")

if __name__ == "__main__":
    find_failed_logins()
