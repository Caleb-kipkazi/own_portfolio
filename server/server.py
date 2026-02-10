from http.server import HTTPServer, BaseHTTPRequestHandler
from server.router import route_request
import os


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        route_request(self, method="GET")

    def do_POST(self):
        route_request(self, method="POST")

    def do_HEAD(self):
        route_request(self, "HEAD")

if __name__ == "__main__":
    # 🔴 THIS IS THE MOST IMPORTANT PART
    PORT = int(os.environ.get("PORT", 8000))

    server = HTTPServer(("0.0.0.0", PORT), RequestHandler)

    print(f"Server running on port {PORT}")  # NOT localhost
    server.serve_forever()
