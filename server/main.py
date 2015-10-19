import socket
from thread import *

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #host_name = socket.gethostname()
    host_name = '127.0.0.1'
    host_port = 4248
    server.bind((host_name, host_port))
    server.listen(5)
    conn, addr = server.accept()
    while 1:
        data = conn.recv(1024)
        print data
        
def music_thread(conn):
    conn.send("You are now connected! Feel free to play some music!")
    while 1:
        data = conn.recv(1024)
        print data
    conn.close()

if __name__ == '__main__':
    main()
