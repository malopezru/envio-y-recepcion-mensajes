import socket
import threading

def handle_client(client_socket, username):
    while True:
        try:
            # Receive data from the client
            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                break

            # Broadcast the received data to all clients
            broadcast(f'{data}'.encode('utf-8'))

        except Exception as e:
            print(f"Error handling client {username}: {e}")
            break

    # Remove the client from the list
    remove_client(client_socket)
    client_socket.close()

def broadcast(message):
    for client in clients:
        client.send(message)

def remove_client(client_socket):
    if client_socket in clients:
        clients.remove(client_socket)

# Server configuration
host = '127.0.0.1'
port = 12345

# Create a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(2)  # Allow up to 2 clients

print(f"Server listening on {host}:{port}")

clients = []

while True:
    # Accept a new client connection
    client_socket, addr = server_socket.accept()
    print(f"Accepted connection from {addr}")

    # Get the username from the client
    username = client_socket.recv(1024).decode('utf-8')
    clients.append(client_socket)

    # Send a welcome message to the new client
    client_socket.send(f"Welcome, {username}!".encode('utf-8'))

    # Start a new thread to handle the client
    client_thread = threading.Thread(target=handle_client, args=(client_socket, username))
    client_thread.start()