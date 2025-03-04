from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html>
<head>
<title>My webserver</title>
</head>
<body>
<h1>Top five Revenue generating Software Companies</h1>
<ol>
<li>Microsoft</li>
<li>Oracle</li>
<li>Salesforce</li>
<li>IBM</li>
<li>Intuit</li>
</ol>
</body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8005)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()