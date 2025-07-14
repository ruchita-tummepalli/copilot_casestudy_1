import os
import platform

def print_system_uptime():
    system = platform.system()
    uptime = None

    if system == "Windows":
        # On Windows, use 'net stats srv' and parse the output
        try:
            output = os.popen('net stats srv').read()
            for line in output.split('\n'):
                if "Statistics since" in line:
                    print("System Uptime:", line.strip())
                    return
            print("Could not determine uptime on Windows.")
        except Exception as e:
            print(f"Error: {e}")
    elif system in ("Linux", "Darwin"):
        # On Unix-like systems, read /proc/uptime or use 'uptime' command
        try:
            if os.path.exists('/proc/uptime'):
                with open('/proc/uptime', 'r') as f:
                    seconds = float(f.readline().split()[0])
                    hours = int(seconds // 3600)
                    minutes = int((seconds % 3600) // 60)
                    print(f"System Uptime: {hours} hours, {minutes} minutes")
            else:
                output = os.popen('uptime -p').read().strip()
                print("System Uptime:", output)
        except Exception as e:
            print(f"Error: {e}")
    else:
        print(f"Unsupported operating system: {system}")

if __name__ == "__main__":
    print_system_uptime()
