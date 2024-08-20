import socket

def client_program():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_ip = '192.168.1.66'  # Replace with the server's IP address
    server_port = 9999
    
    try:
        client.connect((server_ip, server_port))
        print(f"Connected to {server_ip}:{server_port}")
        
        while True:
            command = input("Enter command: ")
            if command.lower() == 'exit':
                client.send(command.encode('utf-8'))
                break
            
            if command:
                client.send(command.encode('utf-8'))
                
                while True:
                    response = client.recv(4096).decode('utf-8')
                    if response:
                        print(response)
                        break
                    
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client.close()

if __name__ == '__main__':
    client_program()
