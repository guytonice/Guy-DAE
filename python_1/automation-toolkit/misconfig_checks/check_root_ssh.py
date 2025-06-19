def check_root_ssh(file="/etc/ssh/sshd_config"):
    try:
        with open(file, "r") as f:
            for line in f:
                if "PermitRootLogin" in line:
                    print("SSH Root Login Config:", line.strip())
    except FileNotFoundError:
        print("SSH config file not found or inaccessible.")

if __name__ == "__main__":
    check_root_ssh()
