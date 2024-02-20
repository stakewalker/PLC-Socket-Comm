import socket
import sys
import struct
# from rich import print  # Recommended for better visualization

socketc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create Socket
server_address = ('192.168.1.123', 2020)  # Assign IP and port for server
socketc.bind(server_address)  # TCP 2020

print('starting up on {} port {}'.format(*server_address))
socketc.listen(1)
my_int = 4321
msg_to_send = my_int.to_bytes(4, byteorder='big')

while True:
    # Wait for a connection
    print("Waiting for connection")
    connection, client_address = socketc.accept()
    
    try:
        print("Connection from IP...", client_address)

        # Receive data in chunks (segments)
        while True:
            # Adjust it according to the data type
            # data = str(connection.recv(99))  # Receive bytes as string
            # data = struct.unpack('>H', connection.recv(99))[0]  # Receive INT
            # data = struct.unpack('>f', connection.recv(99))[0]  # Receive REAL
            data = struct.unpack('>l', connection.recv(99))[0]  # Receive DINT
            # data = bool(connection.recv(1)[0])  # Receive BOOL
            print(f"Received {data}")
            if data:
                print("Returning data to client")
                connection.sendall(msg_to_send)
            else:
                print("No data from client...", client_address)
                break

    finally:
        # Close connection
        connection.close()
