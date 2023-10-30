from http.server import HTTPServer, BaseHTTPRequestHandler
import os
from urllib.parse import parse_qs
import socket

a = "test.html"

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

print("mande para seu amigos se conectar em: http://" + ip_address + ":8080")


class Servidor(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/{}'.format(a)

        if self.path.endswith('.html'):
            content_type = 'text/html'
        elif self.path.endswith('.jpg'):
            content_type = 'image/jpeg'
        elif self.path.endswith('.zip'):
            content_type = 'application/zip'
        elif self.path.endswith('.txt'):
            content_type = 'text/plain'
        else:
            content_type = 'text/plain'

        try:
            if not self.path.endswith('.zip'):
                file_to_open = open(self.path[1:], 'rb').read()
                self.send_response(200)
            else:
                with open(self.path[1:], 'rb') as binary_file:
                    file_to_open = binary_file.read()
                self.send_response(200)
        except FileNotFoundError:
            file_to_open = "O arquivo não foi encontrado"
            self.send_response(404)

        self.send_header('Content-type', content_type)
        self.end_headers()

        if not self.path.endswith('.zip'):
            self.wfile.write(file_to_open)
        else:
            self.send_header('Content-Disposition', f'attachment; filename="{os.path.basename(self.path)}')
            self.wfile.write(file_to_open)

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')

        post_params = parse_qs(post_data)
        user_name = post_params.get('user_name', [''])[0]

        print(f"User Name: {user_name}")

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        response = f"Você enviou: {user_name}"
        self.wfile.write(response.encode('utf-8'))

if __name__ == '__main__':
   # print("Insira o nome do arquivo e a extensão dele (por exemplo, arquivo.zip):")
   # a = input()
    httpd = HTTPServer(('0.0.0.0', 8080), Servidor)
    httpd.serve_forever()
