from http.server import HTTPServer, BaseHTTPRequestHandler
from io import BytesIO
import requests, json

list_of_all_items = []

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):


    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'{"message": "Hello, world!"}')
        for item in list_of_all_items:
            self.wfile.write(item)
    
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
        list_of_all_items.append(body)


# Start the HTTP Server
PORT = 8080

httpd = HTTPServer(('localhost', PORT), SimpleHTTPRequestHandler)
print("serving at port", PORT)
httpd.serve_forever()

# Assignment
# Post your name and age and make the http server return it
# response = requests.post(
#     'localhost:8080',
#     params={'name': 'murat', 'age': 28}
# )

# print("code:\n" + str(response.status_code))
# print("\n==================\n")
# print("headers:\n" + str(response.headers))
# print("\n==================\n")
# print("content:\n" + str(response.text))
# print("\n==================\n")
# Extra credit
# Make the http server return a list of all the names and ages that have been posted
