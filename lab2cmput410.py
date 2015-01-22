import socket
import sys
from thread import *
# AF = address family
try:
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as msg:
    print('Failed to create socket!')
    print('Error code: ' + str(msg[0]) + ', error message ' + msg[1])
    sys.exit()
print('Socket Created successfully');

host = ''
port = 8888

try:
    s.bind((host, port))
except socket.error:
    msg = str(socket.error)
    print('Bind failed! Error code: ' + str(msg[0]) + ' , message ' + str(msg[1]))
    sys.exit()
print('Socket bind complete.')
s.listen(10)
print('Socket is now listening.')

def clientthread(conn):
    while True:
        data = conn.recv(1024)
        if not data:
            break 
            #data2 = str(data)
            #data2 = data2[len(data2)-2]
        reply = str(data)
        reply = reply.rstrip("\r\n")
        if reply == chr(27):
            break;
        else:
            conn.sendall('Hello ' + reply.encode('UTF8') + '\r\n')
    conn.close()

while True:
    conn, addr = s.accept()
    print('Connected with ' + addr[0] + ':' + str(addr[1]))    
    start_new_thread(clientthread ,(conn,))

s.close()
#try:
    #remote_ip = socket.gethostbyname(host)
#except socket.gaierror:
    #print('Host name could not be resolved')
    #sys.exit()
#print('IP address of ' + host + ' is ' + remote_ip)
#s.connect((remote_ip, port))
#print('Socket connected to ' + host + ' on ip ' + remote_ip)

#message = 'GET / HTTP/1.1\r\n\r\n'
#try:
    #s.sendall(message.encode("UTF8"))
#except socket.error:
    #print('Send failed!')
    #sys.exit()
#print('Message sent successfully.')

#reply = s.recv(4096)
#print(reply)
#s.close()
