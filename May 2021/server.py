import socket
import sys

# creating a socket
def create_socket():
	try:
		global host
		global port
		global s
		host ='192.168.1.5'
		port=9999
		s=socket.socket()

	except socket.error as msg:
		print('Socket Error: '+str(msg))

# binding the socket and listening for connections. 
def bind_socket():
	try:
		global host
		global port
		global s
		print('Binding the port'+str(port))
		s.bind((host,port))
		s.listen(5)
	except socket.error as msg:
		print('Socket binding error: '+str(msg)+'\n'+'Retrying')
		bind_socket()

# established connection with a client (Socket must be listening)
def socket_accept():
	conn,address = s.accept()
	print('connection has been established'+'IP'+address[0]+'port'+str(address[1]))
	send_command(conn)
	conn.close()

def send_command(conn):
	while True:
		cmd = input
		if cmd == 'quit':
			conn.close()
			s.close()
			sys.exit()
		if len(str.encode(cmd))>0:
			conn.send(str.encode(cmd))
			# echo hey
			client_response = str(conn.recv(1024),'utf-8')
			print(client_response,end='')


def main():
	create_socket()
	bind_socket()
	socket_accept()

main()