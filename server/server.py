from http.server import HTTPServer, BaseHTTPRequestHandler
from server.router import route_request


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        route_request(self, method="GET")

    def do_POST(self):
        route_request(self, method="POST")

if __name__ == "__main__":
    server = HTTPServer(("localhost", 8000), RequestHandler)
    print("Server running at http://localhost:8000")
    server.serve_forever()
