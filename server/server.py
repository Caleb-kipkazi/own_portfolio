import os
from http.server import HTTPServer, BaseHTTPRequestHandler
from server.router import route_request


class RequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        route_request(self, "GET")

    def do_POST(self):
        route_request(self, "POST")

    def do_HEAD(self):
        route_request(self, "HEAD")

    # Optional: remove default logging noise
    def log_message(self, format, *args):
        return


if __name__ == "__main__":
    PORT = int(os.environ.get("PORT", 8000))

    server = HTTPServer(("0.0.0.0", PORT), RequestHandler)

    print(f"Server running on port {PORT}")
    server.serve_forever()
