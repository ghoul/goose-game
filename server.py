import http.server
import socketserver
import os
import gzip

PORT = 8080

class GzipHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Check if the requested file ends with .gz extension
        if self.path.endswith('.gz'):
            self.send_response(200)
            self.send_header('Content-Encoding', 'gzip')
            self.end_headers()

            # Open and send the pre-compressed file
            with open(os.getcwd() + self.path, 'rb') as f:
                self.wfile.write(f.read())
        else:
            # Serve non-gzipped files as usual
            return http.server.SimpleHTTPRequestHandler.do_GET(self)

# Start the server with the custom handler
with socketserver.TCPServer(("", PORT), GzipHandler) as httpd:
    print("Serving at port", PORT)
    httpd.serve_forever()
