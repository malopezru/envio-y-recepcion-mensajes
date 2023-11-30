from generate_key_pair import generate_key_pair
import socket
import threading
from digital_signature import digital_signature
from sha256 import calcular_sha256


def receive_messages():
    while True:
        try:
            # Receive and print messages from the server
            data = client_socket.recv(1024).decode('utf-8')
            print("signature: " + data)
            data = client_socket.recv(1024).decode('utf-8')
            print("message: " + data)
        except Exception as e:
            print(f"Error receiving message: {e}")
            break


def send_messages():
    while True:
        try:
            # Get user input and send it to the server
            message = input()
            if message == "verify":
                original_message = input("Enter Message received: ")
                signature = input("Enter Signature received: ")
                public_key = input("Enter public_key received: ")
                nModule = input("Enter module received: ")
                if verify_signature(original_message, int(signature), public_key, nModule):
                    print("Message is authentic")
                else:
                    print("Message has been tampered with.")
            else:
                signature = digital_signature(message, module, private_key)
                client_socket.send(message.encode('utf-8'))
                client_socket.send(str(signature).encode('utf-8'))
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
module, public_key, private_key = generate_key_pair()
print("Your public Key is: " + str(public_key))
print("Your private Key is: " + str(private_key))
print("Your module is: " + str(module))
client_socket.send(username.encode('utf-8'))

# Start separate threads for sending and receiving messages
receive_thread = threading.Thread(target=receive_messages)
send_thread = threading.Thread(target=send_messages)

# Start the threads
receive_thread.start()
send_thread.start()


def verify_signature(original_message, signature, public_key, module):
    message = bytes(original_message, 'utf-8')
    hash = int.from_bytes(
        bytes(calcular_sha256(message), "utf-8"), byteorder='big')
    hashFromSignature = pow(signature, int(public_key), int(module))
    if hash == hashFromSignature:
        return True
    return False
