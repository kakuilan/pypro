#!/usr/bin/python3
# coding: utf-8
# cgi web服务器

from http.server import HTTPServer, CGIHTTPRequestHandler

port = 8088
httpd = HTTPServer(('', port), CGIHTTPRequestHandler)
print("Starting cgi httpd on port:" + str(httpd.server_port))
httpd.serve_forever()
