import socket
import threading

# Server configuration
HOST = '127.0.0.1'  # Localhost
PORT = 12345        # Port number

# Start the server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []  # List to keep track of connected clients
nicknames = []  # List to store client nicknames

# Broadcast messages to all clients
def broadcast(message):
    for client in clients:
        client.send(message)

# Handle individual client
def handle_client(client):
    while True:
        try:
            # Receive and broadcast messages
            message = client.recv(1024)
            broadcast(message)
        except:
            # Remove disconnected client
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f"{nickname} has left the chat!".encode('utf-8'))
            nicknames.remove(nickname)
            break

# Accept new connections
def receive_connections():
    print("Server is running and listening...")
    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}")

        # Request and store nickname
        client.send("NICK".encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        nicknames.append(nickname)
        clients.append(client)

        print(f"Nickname of the client is {nickname}")
        broadcast(f"{nickname} joined the chat!".encode('utf-8'))
        client.send("Connected to the server!".encode('utf-8'))

        # Start handling client in a new thread
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

receive_connections()
