#Нужно для работы gettoken.py
from http.server import HTTPServer, CGIHTTPRequestHandler
server_adres = ("", 8088)
httpd = HTTPServer(server_adres, CGIHTTPRequestHandler)
httpd.serve_forever()