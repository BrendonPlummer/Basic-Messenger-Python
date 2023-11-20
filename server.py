import socket
import threading

# Server configuration
HOST = '127.0.0.1'
PORT = 5555
# Create a socket 
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT)) # Bind the socket to a specific address and port 
server_socket.listen() # Listen for incoming connections
print(f"Server listening on {HOST}:{PORT}")
clients = [] # List to store client sockets

# Function to handle client connections
def handle_client(client_socket):
    while True:
        try:
            # Receive data from the client
            data = client_socket.recv(1024)
            if not data:
                break
            # Broadcast the received message to all clients
            for client in clients:
                client.send(data)
        except Exception as e:
            print(f"Error: {e}")
            break

# Main server loop
while True:
    # Accept a new connection
    client_socket, client_address = server_socket.accept()
    # Add the new client to the list
    clients.append(client_socket)
    # Start a new thread to handle the client
    client_handler = threading.Thread(target=handle_client, args=(client_socket,))
    client_handler.start()
