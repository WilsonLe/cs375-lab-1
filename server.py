import sys
import threading
from socket import *


def handle_client_socket(client_socket):
    try:
        message = client_socket.recv(1024).decode()
        filename = message.split()[1]
        if filename == "/":
            filename = "/index.html"
        f = open(file=filename[1:], mode="r", encoding="utf-8", errors="ignore")
        output_data = f.read()
        f.close()

        # Send one HTTP header line into socket
        client_socket.send("HTTP/1.1 200 OK\r\n".encode())
        client_socket.send("\r\n".encode())

        # Send the content of the requested file to the client
        for i in range(0, len(output_data)):
            client_socket.send(output_data[i].encode())
        client_socket.send("\r\n".encode())

        client_socket.close()
    except IOError:
        # Send response message for file not found
        client_socket.send("HTTP/1.1 404 Not Found\r\n".encode())
        client_socket.send("\r\n".encode())

        # Read 404 Not Found
        f = open(file="./404.html", mode="r", encoding="utf-8", errors="ignore")
        output_data = f.read()
        f.close()

        # Send the content of the requested file to the client
        for i in range(0, len(output_data)):
            client_socket.send(output_data[i].encode())
        client_socket.send("\r\n".encode())

        # Close client socket
        client_socket.close()


def main():
    address = "127.0.0.1"
    port = 7345
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.bind((address, port))
    server_socket.listen()
    print(f"Socket listening {address}:{port}")

    while True:
        client_socket, (addr, port) = server_socket.accept()
        print(f"Serving {addr}:{port}")
        thread = threading.Thread(target=handle_client_socket, args=(client_socket,))
        thread.start()
        thread.join()

    server_socket.close()

    sys.exit()  # Terminate the program after sending the corresponding data


if __name__ == "__main__":
    main()
