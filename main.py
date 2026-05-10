import socket

def process_request(client_socket):

    #Read data from client
    r = client_socket.recv(1024)
    decoded_r = r.decode()
    print(f"\nReceived data: {decoded_r}\n")

    r_entries = decoded_r.split('\r\n')

    method, path, version = r_entries[0].split(' ')[1]

    if path == '/':
        #Send a 200 OK response
        client_socket.send(b"HTTP/1.1 200 OK\r\n\r\n")
    else:
        client_socket.send(b"HTTP/1.1 404 Not Found\r\n\r\n")
    client_socket.close()

def main():
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    server_socket.listen()
    
    try:
        while True:

            #Wait for a connection
            print("Waiting for connection...")
            client_socket, addr = server_socket.accept()

            print(f"Connection from {addr} has been established.")

            #Handles the client request
            process_request(client_socket)

    except KeyboardInterrupt:
        print("\nServer is shutting down")
    finally:

        #Clean up the server socket
        server_socket.close()
        print("\nServer has been shut down")

if __name__ == "__main__":
    main()