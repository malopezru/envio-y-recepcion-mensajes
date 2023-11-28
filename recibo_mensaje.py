#Recibir mensaje
IP = "10.203.0.202"
PORT = 5003

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((IP, PORT))
print(f"start listening to {IP}:{PORT}")
while True:
    data, addr = sock.recvfrom(1024)
    print(f"received message: {data}")