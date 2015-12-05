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
    music_thread(conn)
        
def music_thread(conn):
    conn.send("You are now connected! Feel free to play some music!")
    
    while 1:
        MSGLEN = 1024
        chunks = ''
        bytes_recd = 0
        while bytes_recd < MSGLEN:
            chunk = conn.recv(min(MSGLEN - bytes_recd, 1024))
            if chunk == '':
                raise RuntimeError("Socket broken")
            chunks += chunk
            bytes_recd = bytes_recd + len(chunk)
        print chunks
    conn.close()

if __name__ == '__main__':
    main()
