import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = 10000
address = 'localhost'
server_address = (address, port)
s.bind(server_address)

data, from_address = s.recvfrom(2)
print data
print from_address

sent_bytes = s.sendto('receipt done', from_address)
print sent_bytes

s.close()
