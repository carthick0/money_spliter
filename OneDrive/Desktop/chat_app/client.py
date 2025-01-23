import socket
import threading

# Client configuration
HOST = '127.0.0.1'  # Server address
PORT = 12345        # Server port

# Connect to the server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

# Receive messages from the server
def receive_messages():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == "NICK":
                client.send(nickname.encode('utf-8'))
            else:
                print(message)
        except:
            print("An error occurred! Exiting...")
            client.close()
            break

# Send messages to the server
def send_messages():
    while True:
        message = f"{nickname}: {input('')}"
        client.send(message.encode('utf-8'))

# Ask for the client's nickname
nickname = input("Enter your nickname: ")

# Start threads for sending and receiving
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

send_thread = threading.Thread(target=send_messages)
send_thread.start()
