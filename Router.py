import os

from http_response import HttpResponse

class Router():
    
    def route(self, file_dir, http_request):
        if http_request.path.startswith("/files/"):
            base = os.path.basename(http_request.path)
            path = os.path.join(file_dir, base)

            if http_request.method == "POST":
                res = self._post_file_content(path, http_request.body)
                if res != None:
                    return HttpResponse(status = "201 Created")

            elif http_request.method == "GET":
                content = self._get_file_content(path)
                if content != None:
                    return HttpResponse(status = "200 OK", content_type = "text/plain", body = content)

            
            return self._get_404_response()


        if http_request.path == "/user-agent":
            user_agent = http_request.headers["User-Agent"]
            return HttpResponse(status = "200 OK", content_type = "text/plain", body = user_agent)

        if http_request.path == "/":
            return HttpResponse(status = "200 OK")

        return self._get_404_response()

    def _get_404_response(self):
        return HttpResponse("404 Not Found")

    def _get_file_content(self, path):
        try:
            with open(path, 'r') as f:
                return f.read()
        except:
            return None
    
    def _post_file_content(self, path, content):
        try:
            with open(path, 'w') as f:
                f.write(content)
                return "Ok"
        except:
            return None

        