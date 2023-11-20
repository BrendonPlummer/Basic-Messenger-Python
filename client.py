import socket
import threading

# Server configuration
HOST = '127.0.0.1'
PORT = 5555
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Creates a socket
client_socket.connect((HOST, PORT)) # Connect to the server


#For some reason messaging order seems weird, comes out as expected but doesnt format correctly
# Function to send messages to the server
def send_message():
    while True:
        message = input("\nYou: ") #The input doesnt quite work properly, maybe due to same machine use? Try on seperate machine
        client_socket.send(message.encode())


#Clients still recieve and send messages as expected, recieve seems to not display quite as expected
# Function to receive messages from the server
def receive_message():
    while True:
        try:
            data = client_socket.recv(1024) # Receives data from the server
            if not data:
                break
            print("\nOther: " + data.decode()) # Display the received message
        
        except Exception as e:
            print(f"Error: {e}")
            break

# Start seperate threads for sending and receiving messages
send_thread = threading.Thread(target=send_message)
receive_thread = threading.Thread(target=receive_message)
send_thread.start()
receive_thread.start()
