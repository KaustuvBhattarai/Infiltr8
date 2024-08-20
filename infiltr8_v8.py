import os
import time
import sys
import subprocess
import platform
import socket

def clear_screen():
    """Clear the screen for Windows and Unix-based systems."""
    os.system('cls' if os.name == 'nt' else 'clear')

def animate_intro_art():
    intro_art = """
██╗███╗   ██╗███████╗██╗██╗  ████████╗██████╗  █████╗ 
██║████╗  ██║██╔════╝██║██║  ╚══██╔══╝██╔══██╗██╔══██╗
██║██╔██╗ ██║█████╗  ██║██║     ██║   ██████╔╝╚█████╔╝
██║██║╚██╗██║██╔══╝  ██║██║     ██║   ██╔══██╗██╔══██╗
██║██║ ╚████║██║     ██║███████╗██║   ██║  ██║╚█████╔╝
╚═╝╚═╝  ╚═══╝╚═╝     ╚═╝╚══════╝╚═╝   ╚═╝  ╚═╝ ╚════╝ 
                                                    
CREATED BY KAUSTUV BHATTARAI 
ALL RIGHTS RESERVED 2024
    """
    frames = [
        intro_art
    ]
    
    for frame in frames:
        clear_screen()
        print(frame)
        time.sleep(1)
        sys.stdout.write(f"\r{' ' * 50}\r")  # Clear previous line

def get_system_details():
    """Fetch system details including IP address."""
    try:
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        os_info = platform.platform()
        time_info = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        
        details = f"""
System Details:
- Time: {time_info}
- Hostname: {hostname}
- IP Address: {ip_address}
- OS: {os_info}
        """
        return details
    except Exception as e:
        return f"Error fetching system details: {e}"

def print_system_output():
    messages = [
        "Initializing network interface...",
        "Connecting to remote servers...",
        "Bypassing firewalls...",
        "Establishing secure tunnel...",
        "Encrypting data packets...",
        "Validating security certificates...",
        "Fetching user credentials...",
        "Loading system modules...",
        "Deploying security protocols..."
    ]
    
    for message in messages:
        print(message)
        time.sleep(1)

def start_server():
    """Start the external server and display detailed status updates."""
    print("Initializing infiltration sequence...\n")
    
    # Simulate a system loading effect
    for i in range(10):
        sys.stdout.write(f"\rLoading{' ' * i}{'.' * (10 - i)}")
        sys.stdout.flush()
        time.sleep(0.5)
    
    print("\nServer starting...")
    time.sleep(1)
    
    # Display system details
    print(get_system_details())
    time.sleep(2)
    
    # Print system output
    print_system_output()
    
    # Start the external executable
    try:
        subprocess.Popen(['infiltr8_server.exe'], shell=True)
        print("Server has been successfully launched.\n")
        print("Initiating security protocols...")
        time.sleep(2)
        print("Secure connection established. All systems operational.")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    animate_intro_art()
    input("INFILTR8 V2.87 - KR1NZL3R - 2433WINPY24\nPress Enter to start the server...")
    start_server()
    # Close the terminal window
    if os.name == 'nt':
        os.system('exit')
    elif os.name != 'nt':
        os._exit(0)
