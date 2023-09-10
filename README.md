## EX : 01
# Developing a Simple Webserver
## AIM:
To develop a simple webserver to serve html pages.

## DESIGN STEPS:
### Step 1: 
HTML content creation
### Step 2:
Design of webserver workflow
### Step 3:
Implementation using Python code
### Step 4:
Serving the HTML pages.
### Step 5:
Testing the webserver

## PROGRAM:
```
from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html>
<head>
<title>My webserver</title>
</head>
<body>
<h1>TOP 5 LARGEST SOFTWARE COMPANIES IN THE WORLD</h1>
<ol>
<li>AMAZON</li>
<li>GOOGLE</li>
<li>INFOSYS</li>
<li>ZOHO</li>
<li>COGNIZANT</li>
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
server_address = ('',8003)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()
```

## OUTPUT:


![image](https://github.com/KARPAGAKIRTHIKA/simplewebserver/assets/103020162/53a1387d-e1bc-4e6d-866c-0636427e6a1b)


## RESULT:
The program for implementing simple webserver is executed successfully.
