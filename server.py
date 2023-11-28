import select
import socket
from queue import Queue

# Crear un socket servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 8080))
server_socket.listen(5)

# Crear una cola de prioridad para encolar las solicitudes
queue = Queue()

# Lista de sockets para selección
sockets_list = [server_socket]

while True:
    # Seleccionar sockets disponibles para lectura, escritura, errores
    read_sockets, _, _ = select.select(sockets_list, [], [])

    for sock in read_sockets:
        # Nueva conexión entrante
        if sock == server_socket:
            client_socket, addr = server_socket.accept()
            IP, port = client_socket.getpeername()
            sockets_list.append(client_socket)

        # Datos disponibles en un socket existente
        else:
            # Recibir los datos
            data = sock.recv(1024)
            if data:
                queue.put(data)  # Ajustar el nivel de prioridad


    # Procesar las solicitudes en la cola de prioridad (las de mayor prioridad primero)
    while not queue.empty():
        ver_message = queue.get() #recibe llave publica, mensaje y mensaje encriptado


