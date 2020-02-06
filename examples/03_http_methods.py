from http.server import HTTPServer, BaseHTTPRequestHandler
from io import BytesIO


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'{"message": "Hello, world!"}')

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        self.send_response(200)
        self.end_headers()
        response = BytesIO()
        response.write(b'This is POST request. \n')
        response.write(b'\nReceived: ')
        response.write(body)
        self.wfile.write(response.getvalue())


# Start the HTTP Server
PORT = 8080

httpd = HTTPServer(('localhost', PORT), SimpleHTTPRequestHandler)
print("serving at port", PORT)
httpd.serve_forever()

# Assignment
# Post your name and age and make the http server return it

# Extra credit
# Make the http server return a list of all the names and ages that have been posted
