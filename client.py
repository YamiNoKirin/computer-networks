import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = 10000
address = 'localhost'
server_address = (address, port)

s.sendto('hi', server_address)
data, from_address = s.recvfrom(4)
print data
print from_address

s.close()
