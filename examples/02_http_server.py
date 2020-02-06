from http.server import HTTPServer, BaseHTTPRequestHandler


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hello, world!')


# Start the HTTP Server
PORT = 8080

httpd = HTTPServer(('localhost', PORT), SimpleHTTPRequestHandler)
print("serving at port", PORT)
httpd.serve_forever()

# Assignment:
# Access your http server through your browser
# Do a GET with Postman
# Do a POST with Postman
