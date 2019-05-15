# TCP client
import socket
import logging
import time
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-s', '--server', dest = 'server_addr')
args = parser.parse_args()

logging.basicConfig(format = u'[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s', level = logging.NOTSET)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 10000
server_address = (args.server_addr, port)
mesaj = sys.argv[0]

try:
    logging.info('Handshake cu %s', str(server_address))
    sock.connect(server_address)
    time.sleep(15)
    sock.send("Client - OK")
    data = sock.recv(1024)
    logging.info('Content primit: "%s"', data)

finally:
    logging.info('closing socket')
    sock.close()
