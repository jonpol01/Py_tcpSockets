#!/usr/bin/python
import asyncore
import socket

a = [0 for x in range(10)]
i = 0
class EchoHandler(asyncore.dispatcher_with_send):

    def handle_read(self):
        data = self.recv(8192)
        if data:
            self.send(data)

class EchoServer(asyncore.dispatcher):

    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind((host, port))
        self.listen(5)

    def handle_accept(self):
        pair = self.accept()
        if pair is not None:
            sock, addr = pair
            print 'Incoming connection from %s' % repr(addr)
	    if i == 0:
		a[0] = sock
	    else:
		i+1
	    	a[i] = sock
            handler = EchoHandler(a[i])

server = EchoServer('', 8080)
asyncore.loop()
