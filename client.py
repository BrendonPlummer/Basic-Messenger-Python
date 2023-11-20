import socket
import threading

# Server configuration
HOST = '127.0.0.1'
PORT = 5555
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create a socket
client_socket.connect((HOST, PORT)) # Connect to the server

# Function to send messages to the server
def send_message():
    while True:
        message = input("You: ")
        client_socket.send(message.encode())

# Function to receive messages from the server
def receive_message():
    while True:
        try:
            data = client_socket.recv(1024) # Receive data from the server
            if not data:
                break
            print("\nOther: " + data.decode()) # Display the received message
        
        except Exception as e:
            print(f"Error: {e}")
            break

# Start threads for sending and receiving messages
send_thread = threading.Thread(target=send_message)
receive_thread = threading.Thread(target=receive_message)
send_thread.start()
receive_thread.start()
