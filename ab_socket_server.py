import socket
import struct
from rich import print

def main():
    # PLC and PC addresses
    plc_address = ('192.168.1.36', 2021)
    pc_address = ('192.168.1.123', 2020)
    # Create server socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(pc_address)
    server_socket.listen(1)
    print(f'Listening on {pc_address[0]} port {pc_address[1]}')

    while True:
        # Wait for a connection
        print('Waiting for connection...')
        connection, client_address = server_socket.accept()
        try:
            print(f'Connection established with {client_address}')
            # Send SINT[4] array
            data_to_send = bytes([18, 222, 33, 44])
            connection.sendall(data_to_send)
            print('Array sent (SINT[4]):', [i for i in data_to_send])
            # Receive data from PLC
            received_data = [i for i in connection.recv(16)]
            print('Data received from PLC:', list(received_data))
        finally:
            # Close the connection
            connection.close()

if __name__ == "__main__":
    main()
