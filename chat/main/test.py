from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs
import socket

a = "index.html"
messages = []

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

print("Mande seus amigos se conectarem em: http://" + ip_address + ":8080")

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
            with open(self.path[1:], 'rb') as file:
                file_to_open = file.read()
                self.send_response(200)
        except FileNotFoundError:
            file_to_open = "O arquivo não foi encontrado"
            self.send_response(404)

        self.send_header('Content-type', content_type)
        self.end_headers()

        if self.path.endswith('.html'):
            chat_content = self.get_chat_html()
            file_to_open = file_to_open.replace(b'<!-- CHAT_CONTENT -->', chat_content.encode('utf-8'))

        self.wfile.write(file_to_open)

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')

        post_params = parse_qs(post_data)
        user_name = post_params.get('user_name', [''])[0]
        mensagem = post_params.get('mensagem', [''])[0]

        if user_name and mensagem:
            messages.append((user_name, mensagem))

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        response = f"Você enviou: {user_name} - Mensagem: {mensagem}"
        self.wfile.write(response.encode('utf-8'))

    def get_chat_html(self):
        chat_content = ""
        for user, message in messages:
            chat_content += f'<p><strong>{user}:</strong> {message}</p>'
        return chat_content

httpd = HTTPServer(('0.0.0.0', 8080), Servidor)
httpd.serve_forever()
