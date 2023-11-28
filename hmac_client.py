from generate_hmac import hmac
import socket
import threading

def receive_messages():
    while True:
        try:
            # Receive and print messages from the server
            data = client_socket.recv(1024).decode('utf-8')
            print("message: " + data)
            data = client_socket.recv(1024).decode('utf-8')
            print(data)
        except Exception as e:
            print(f"Error receiving message: {e}")
            break

def send_messages():
    while True:
        try:
            # Get user input and send it to the server
            message = input()
            if message == "verify":
                received_message = input("Received Message: ")
                received_hmac = input("Received HMAC: ")
                secret_key = input("Secret Key: ")
                if verify_hmac(received_message, received_hmac, secret_key):
                    print("Message is authentic")
                else:
                    print("Message has been tampered with.")
            else:
                hashedMessage = hmac(key, message)
                client_socket.send(hashedMessage.encode('utf-8'))
                client_socket.send(message.encode('utf-8'))
        except Exception as e:
            print(f"Error sending message: {e}")
            break

# Server configuration
host = '127.0.0.1'
port = 12345

# Create a socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((host, port))

# Get the username from the user
username = input("Enter your username: ")
key = input("Enter your secret key: ")
client_socket.send(username.encode('utf-8'))

# Start separate threads for sending and receiving messages
receive_thread = threading.Thread(target=receive_messages)
send_thread = threading.Thread(target=send_messages)

# Start the threads
receive_thread.start()
send_thread.start()

def verify_hmac(received_message, received_hmac, secret_key):
    regenerated_hmac = hmac(secret_key, received_message)
    if regenerated_hmac == received_hmac:
        return True
    return False