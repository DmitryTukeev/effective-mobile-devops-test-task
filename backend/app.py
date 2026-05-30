import os
from http.server import BaseHTTPRequestHandler, HTTPServer

# 1. Best Practice: Конфигурация через переменные окружения (12-Factor App)
PORT = int(os.getenv('BACKEND_PORT', '8080'))
# Явно указываем 0.0.0.0
HOST = '0.0.0.0' 

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # 2. Правильный роутинг: отвечаем только на корневой путь
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain; charset=utf-8')
            self.end_headers()
            self.wfile.write(b"Hello from Effective Mobile!")
        else:
            # 3. Корректная обработка остальных запросов
            self.send_response(404)
            self.send_header('Content-Type', 'text/plain; charset=utf-8')
            self.end_headers()
            self.wfile.write(b"404 Not Found")

if __name__ == '__main__':
    server_address = (HOST, PORT)
    httpd = HTTPServer(server_address, SimpleHandler)
    print(f"Starting backend server on {HOST}:{PORT}...")
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        httpd.server_close()
        print("Server stopped.")
