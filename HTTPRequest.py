class HTTPRequest():
    def __init__(self, raw):
        
        header, body = raw.split('\r\n\r\n')
        
        self.parse_headers(header)
        self.parse_firstline(header.split('\r\n')[0])
        self.parse_body(body)
    
    def parse_headers(self, headers):
        header_except_line = headers.split('\r\n')[1:]
        self.headers = {}
        for header in header_except_line:
            line = header.split(':', 1)
            self.headers[line[0]] = line[1].strip()
        pass

    def parse_firstline(self, firstline):
        line = firstline.split(' ')
        self.method = line[0]
        self.path = line[1]
        self.version = line[2]
        pass