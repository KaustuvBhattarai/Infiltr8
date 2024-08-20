# INFILTR8

This is a Python application that listens for connections and allows remote command execution. It uses socket programming to communicate with clients and executes commands received from them.

## Features

- **Remote Command Execution**: The server executes shell commands received from connected clients.
- **Multithreading**: Each client connection is handled in a separate thread.
- **System Details**: Fetches and displays system information including IP address and OS details.
- **Error Handling**: Basic error handling is implemented for command execution and client handling.
- **External Server Launch**: Attempts to start an external executable file (`infiltr8_server.exe`).


## Security Warning :
This server implementation does not include security measures such as authentication or input validation. 

**It is intended for my personal use only and should not be used in a production environment.**
