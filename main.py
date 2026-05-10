import socket
import os
import threading
import sys

def get_response(path, code = '200 OK'):
    # response = b"HTTP/1.1 404 Not Found\r\n\r\n"
    
    response = f"HTTP/1.1 {code}\r\nContent-Type: text/plain\r\nContent-Length: {len(path)}\r\n\r\n{path}".encode()

    return response


def process_request(client_socket, file_dir = None):
    
    #Read data from client
    r = client_socket.recv(1024)
    decoded_r = r.decode()
    print(f"\nReceived data: {decoded_r}\n")
    header, request = decoded_r.split('\r\n\r\n')
    r_entries = header.split('\r\n')
    code = '200 OK'

    method, path, version = r_entries[0].split(' ')
    base = os.path.basename(path)

    if base == "user-agent":
        user_agent = r_entries[2]
        base = user_agent.split(':')[1].strip()

    if "files" in path:
        if method == 'POST':
            cp = os.path.join(file_dir, base)
            code = '201 Created'
            with open(cp, 'w') as f:
                f.write(request)
        else:
            cp = os.path.join(file_dir, base)
            with open(cp, 'r') as f:
                base = f.read()

    res = get_response(base, code)
    client_socket.send(res)
    
    client_socket.close()

def client_thread(client_socket, addr, file_dir = None):
    print(f"Connection from {addr} has been established.")

    #Handles the client request
    process_request(client_socket, file_dir)


def main():
    args = sys.argv
    file_path = None
    if len(args) > 2:
        file_path = args[2]

    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    server_socket.listen()
    
    try:
        while True:

            #Wait for a connection
            print("Waiting for connection...")
            client_socket, addr = server_socket.accept()

            threading.Thread(target=client_thread,args=(client_socket, addr, file_path)).start()

    except KeyboardInterrupt:
        print("\nServer is shutting down")
    finally:

        #Clean up the server socket
        server_socket.close()
        print("\nServer has been shut down")

if __name__ == "__main__":
    main()