import os
import urllib.parse
import mimetypes

# Base directories
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PUBLIC_DIR = os.path.join(BASE_DIR, "public")


def route_request(handler, method):
    path = handler.path
    print(f"DEBUG: Received {method} request for {path}")

    # Remove query parameters if present
    path = path.split("?")[0]

    # -------------------------
    # GET / HEAD REQUESTS
    # -------------------------
    if method in ("GET", "HEAD"):
        send_body = method == "GET"

        if path == "/":
            serve_file(handler, "index.html", send_body)

        elif path == "/about":
            serve_file(handler, "about.html", send_body)

        elif path == "/projects":
            serve_file(handler, "projects.html", send_body)

        elif path == "/contact":
            serve_file(handler, "contact.html", send_body)

        elif (
            path.startswith("/css/")
            or path.startswith("/js/")
            or path.startswith("/assets/")
        ):
            serve_file(handler, path[1:], send_body)

        else:
            handler.send_error(404, "Page Not Found")

    # -------------------------
    # POST REQUESTS
    # -------------------------
    elif method == "POST":

        if path == "/submit-contact":
            content_length = int(handler.headers.get("Content-Length", 0))
            raw_data = handler.rfile.read(content_length).decode("utf-8")
            params = urllib.parse.parse_qs(raw_data)

            name = params.get("name", ["Guest"])[0]
            email = params.get("email", [""])[0]
            message = params.get("message", [""])[0]

            print("New Contact Submission:")
            print("Name:", name)
            print("Email:", email)
            print("Message:", message)

            handler.send_response(200)
            handler.send_header("Content-type", "text/plain")
            handler.end_headers()

            response = f"Success! Thank you {name}. I'll be in touch."
            handler.wfile.write(response.encode("utf-8"))

        else:
            handler.send_error(404, "Post Path Not Found")

    else:
        handler.send_error(405, "Method Not Allowed")


# ---------------------------------------------------
# FILE SERVING FUNCTION (Handles ALL static files)
# ---------------------------------------------------
def serve_file(handler, filename, send_body=True):
    file_path = os.path.join(PUBLIC_DIR, filename)

    if not os.path.exists(file_path) or not os.path.isfile(file_path):
        handler.send_error(404, "File Not Found")
        return

    # Automatically detect content type
    content_type, _ = mimetypes.guess_type(file_path)

    if content_type is None:
        content_type = "application/octet-stream"

    handler.send_response(200)
    handler.send_header("Content-type", content_type)
    handler.send_header("Content-Length", str(os.path.getsize(file_path)))
    handler.end_headers()

    # Don't send body for HEAD requests
    if send_body:
        with open(file_path, "rb") as file:
            handler.wfile.write(file.read())
