"""
== Maitreya server 1.0: ==

Maitreya server is a minimalistic server that serves simple html files.

= Usage =

Running on the 8000 port:
$ python mserver

Running on an specific port:
$ python mserver 8888
"""
import http.server
import socketserver
import sys

class Server:
    """
    Server class to serve simple html files.
    """
    DEFAULT_PORT = 8000        
    
    def run_server(self):
        """
        This method run the server.
        """
        port = self.__validate_port()
        Handler = http.server.SimpleHTTPRequestHandler

        print("==[ Maitreya Server 1.0 ]==\n")
        with socketserver.TCPServer(("", port), Handler) as httpd:
            print("Serving at port", port)
            httpd.serve_forever()

    def __validate_port(self):
        return int(sys.argv[1]) if len(sys.argv) > 1 else self.DEFAULT_PORT

Server().run_server()

