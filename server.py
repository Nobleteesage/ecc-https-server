import http.server
import ssl
server_address= ('localhost', 4443)
handler = http.server.SimpleHTTPRequestHandler
httpd = http.server.HTTPServer(server_address, handler)

# Create a secure SSL context
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile='cert.pem', keyfile='ecc_private.key')

# Wrap the socket with the SSL context
httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

print("✅ HTTPS Server running at https://localhost:4443")
httpd.serve_forever()

