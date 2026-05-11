class Router():
    def __init__(self, HTTPRequest):
        self.HTTPRequest = HTTPRequest
    
    def routes(self):
        if self.HTTPRequest.path == '/':
            return '200 OK'

        if self.HTTPRequest.path == '/user-agent':
            return '200 OK' + self.HTTPRequest.headers['User-Agent']
        else:
            return 'Not Found'