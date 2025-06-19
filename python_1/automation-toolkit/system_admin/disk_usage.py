import shutil

def check_disk_usage(path="/"):
    """Check and print disk usage stats for the given path."""
    total_space, used_space, free_space = shutil.disk_usage(path)
    total_gb = total_space // (2**30)
    used_gb = used_space // (2**30)
    free_gb = free_space // (2**30)

    # Decision structure
    if free_gb < 10:
        status = "Warning: Low disk space!"
    else:
        status = "Disk space is sufficient."

    # Print using three different data types
    print(f"Total: {total_gb} GB")         # int
    print(f"Used: {used_gb} GB")
    print(f"Free: {free_gb} GB")
    print(f"Status: {status}")             # str
    print(f"Type of free_gb: {type(free_gb)}")  # type object

    return [total_gb, used_gb, free_gb]    # list (sequence)

def main():
    # Looping structure and list iteration
    results = check_disk_usage()
    for index, value in enumerate(results):
        print(f"Disk part {index+1} usage: {value} GB")

if __name__ == "__main__":
    main()
