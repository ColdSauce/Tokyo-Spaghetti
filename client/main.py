import socket
import pyaudio
import sys


def send_music(s):
    # So many caps..
    ONE_KILOBYTE= 1024
    chunk_size = ONE_KILOBYTE
    FORMAT = pyaudio.paUInt8
    CHANNELS = 1 
    RATE = 44100
    audi = pyaudio.PyAudio()
    stream = audi.open(format = FORMAT,
              channels=CHANNELS,
              rate=RATE,
              frames_per_buffer=chunk_size,
              input=True
              )
    channel_map = (0,1)
    if s is None:
        print "stop what r u doing"
        raise Exception('Socket was None')
    # Amazing UX -- the only way to stop is to ctrl-c :p
    data_from_stream = ''
    while 1:
        bytes_read = 0
        while bytes_read < ONE_KILOBYTE:
            data_from_stream = data_from_stream + stream.read(chunk_size)
            bytes_read = bytes_read + 1
        #bytes_read = bytes_read + 1
        #data_from_stream = data_from_stream + stream.read(chunk_size)
        #print str(bytes_read)
        
        
        data_from_stream = ""
        s.send(str(data_from_stream))

def is_ip_address_valid(ip):
    try:
        socket.inet_aton(ip)
    except socket.error:
        return False
    else:
        return True

def is_port_valid(port):
    return 1 < port or port < 65535

def other_main():
    send_music("")

def main():
    print "Howdy, partner! Welcome to Tokyo Spaghetti."
    print "Enter your server's ip address."
    ip = raw_input('>> ')
    print "Now enter your server's port."
    port = raw_input('>> ')

    while not is_ip_address_valid(ip):
        print "Check your ip and try again."
        ip = raw_input(">> ")

    while not is_port_valid(port):
        print "Check your port and try again."
        port = raw_input(">> ")

    print "Connecting to the server."

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip,int(port)))
    send_music(s)

if __name__ == '__main__':
    main()
