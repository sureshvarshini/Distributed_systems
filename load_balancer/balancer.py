from http.server import HTTPServer, BaseHTTPRequestHandler
import threading

HOST = "10.6.33.155"
PORT1 = 9999
PORT2 = 9998


class CompanyHTTP1(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()

        self.wfile.write(bytes("<html><body><h1>I RUN ON SERVER 1</h1></body></html>", "utf-8"))


class CompanyHTTP2(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()

        self.wfile.write(bytes("<html><body><h1>I RUN ON SERVER 2</h1></body></html>", "utf-8"))


def startServer1():
    server1 = HTTPServer((HOST, PORT1), CompanyHTTP1)
    server1.serve_forever()
    server1.server_close()
    print("Server1 now running")


def startServer2():
    server2 = HTTPServer((HOST, PORT2), CompanyHTTP2)
    server2.serve_forever()
    server2.server_close()
    print("Server2 now running")


t1 = threading.Thread(target=startServer1)
t2 = threading.Thread(target=startServer2)
t1.start()
t2.start()
