import socket 

stream_socket = socket.socket( socket.AF_INET, socket.SOCK_STREAM )

server="localhost"
port=80

server_address = ((host, port))
stream_socket.connect(server_address)

# Send data
message = 'message'
stream_socket.sendall(message)
 
# response
data = stream_socket.recv(10)
print data
 