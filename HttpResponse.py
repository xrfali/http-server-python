class HttpResponse():
    def __init__(self, status, content_type, body):
        self.version = "HTTP/1.1"
        self.status = status
        self.content_type = content_type
        self.body = body
    
    def send(self, client_socket):
        response = ''
        if len(self.body) == 0:
            response = f"{self.version} {self.status}\r\n\r\n".encode()
        else:    
            response = f"{self.version} {self.status}\r\nContent-Type: {self.content_type}\r\nContent-Length: {len(self.body)}\r\n\r\n{self.body}".encode()
        
        client_socket.send(response)
        