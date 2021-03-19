import http.server, socketserver
import sys, ssl

def main(argv):
	PORT = ''
	if sys.argv[1] == '-p':
		PORT = sys.argv[2]
	else:
		print("Mauvais argument")
		sys.exit(2)
	Handler = http.server.SimpleHTTPRequestHandler
	https = socketserver.TCPServer(('', int(PORT)), Handler)
	https.socket = ssl.wrap_socket(https.socket, keyfile='key.pem', certfile='cert.pem', server_side=True)
	print("server is running at https://localhost:%s" % (PORT))
	https.serve_forever()

main(sys.argv)