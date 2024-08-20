import requests
import time
import keyboard

def get_public_ip():
    """Fetch the public IP address of the machine."""
    try:
        # Use a public IP address API service
        response = requests.get('https://api.ipify.org?format=json')
        response.raise_for_status()  # Raise an error for bad status codes
        ip_info = response.json()
        return ip_info.get('ip')
    except requests.RequestException as e:
        return f"Error fetching IP address: {e}"

def display_ip_until_escape():
    """Continuously display the public IP address until the Escape key is pressed."""
    print("Press ESC to stop viewing the IP address.")
    
    last_ip = None
    while True:
        if keyboard.is_pressed('esc'):
            print("Escape key pressed. Exiting...")
            break
        
        public_ip = get_public_ip()
        
        # Update display only if IP has changed
        if public_ip != last_ip:
            print(f"\rYour public IP address is: {public_ip}", end="")
            last_ip = public_ip
        
        time.sleep(5)  # Update every 5 seconds

if __name__ == "__main__":
    display_ip_until_escape()
