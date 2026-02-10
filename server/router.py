import os
import urllib.parse

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PUBLIC_DIR = os.path.join(BASE_DIR, "public")

def route_request(handler, method):
    path = handler.path
    print(f"DEBUG: Received {method} request for {path}") # Helps you debug in terminal

    # --- GET METHOD ---
    if method == "GET":
        if path == "/":
            serve_file(handler, "index.html")
        elif path == "/about":
            serve_file(handler, "about.html")
        elif path == "/projects":
            serve_file(handler, "projects.html")
        elif path == "/contact":
            serve_file(handler, "contact.html")
        elif path.startswith("/css/") or path.startswith("/js/") or path.startswith("/assets/"):
            serve_file(handler, path[1:])
        else:
            handler.send_error(404, "Page Not Found")

    # --- POST METHOD ---
    elif method == "POST":
        if path == "/submit-contact":
            # 1. Get data length
            content_length = int(handler.headers['Content-Length'])
            # 2. Read raw data
            raw_data = handler.rfile.read(content_length).decode('utf-8')
            # 3. Parse data
            params = urllib.parse.parse_qs(raw_data)
            
            name = params.get('name', ['Guest'])[0]
            
            # --- RESPONSE ---
            handler.send_response(200)
            handler.send_header("Content-type", "text/plain")
            handler.end_headers()
            
            success_response = f"Success! Thank you {name}. I'll be in touch."
            handler.wfile.write(success_response.encode('utf-8'))
        else:
            print(f"DEBUG: POST Path '{path}' not recognized")
            handler.send_error(404, "Post Path Not Found")

def serve_file(handler, filename):
    file_path = os.path.join(PUBLIC_DIR, filename)

    if not os.path.exists(file_path):
        handler.send_error(404)
        return

    # Proper MIME types are crucial for CSS/JS to work
    if filename.endswith(".css"):
        content_type = "text/css"
    elif filename.endswith(".js"):
        content_type = "application/javascript"
    elif filename.endswith(".png"):
        content_type = "image/png"
    elif filename.endswith(".jpg"):
        content_type = "image/jpeg"
    else:
        content_type = "text/html"

    handler.send_response(200)
    handler.send_header("Content-type", content_type)
    handler.end_headers()

    with open(file_path, "rb") as f:
        handler.wfile.write(f.read())