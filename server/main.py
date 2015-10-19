import socket
from thread import *

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host_name = '0.0.0.0' 
    host_port = 4248
    print "ip: {} port: {}".format('no lolzard', host_port)
    server.bind((host_name, host_port))
    server.listen(5)
    conn, addr = server.accept()
    while 1:
        data = conn.recv(1024)
        if data:
            print data
        
def music_thread(conn):
    conn.send("You are now connected! Feel free to play some music!")
    while 1:
        data = conn.recv(1024)
        print data
    conn.close()

if __name__ == '__main__':
    main()
