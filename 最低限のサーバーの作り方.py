import json
from http.server import BaseHTTPRequestHandler, HTTPServer

class RequestHandler(BaseHTTPRequestHandler):
    def _send_response(self, status_code, response_data):
        self.send_response(status_code)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(response_data).encode('utf-8'))

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        request_data = json.loads(post_data)

        # バリデーション処理（簡単な例として、文字列の長さをチェック）
        if len(request_data.get('username', '')) < 3:
            response = {'error': 'Username must be at least 3 characters'}
            self._send_response(400, response)
            return

        # レスポンスの生成
        response = {'message': 'User registered successfully'}
        self._send_response(201, response)

def run_server(server_class=HTTPServer, handler_class=RequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}')
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()
