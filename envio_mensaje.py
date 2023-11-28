import socket

#Envio mensaje
IP = "10.203.0.202"
PORT = 5003
MESSAGE = "The meeting is From 10 pm."

print(f"sending information")
print(f"{MESSAGE} to {IP}:{PORT}")
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(MESSAGE.encode('utf-8'), (IP, PORT))