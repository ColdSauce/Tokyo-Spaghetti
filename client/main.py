import socket
import pyaudio
import sys
import base64


def alt_send(s):
    import wave

    CHUNK = 1024
    FORMAT = pyaudio.paUInt8
    CHANNELS = 2
    RATE = 44100
    RECORD_SECONDS = 15
    WAVE_OUTPUT_FILENAME = "output.wav"

    p = pyaudio.PyAudio()

    SPEAKERS = p.get_default_output_device_info()["hostApi"] #The part I have modified

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK,
                    input_host_api_specific_stream_info=SPEAKERS) #The part I have modified

    print("* recording")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("* done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close() 

def send_music(s):
    # So many caps..
    ONE_KILOBYTE=1024
    chunk_size = ONE_KILOBYTE
    FORMAT = pyaudio.paUInt8
    CHANNELS = 2 
    RATE = 44100
    audi = pyaudio.PyAudio()
    stream = audi.open(format = FORMAT,
              channels=CHANNELS,
              rate=RATE,
              frames_per_buffer=chunk_size,
              input=True
              )
    if s is None:
        print "stop what r u doing"
        raise Exception('Socket was None')
    # Amazing UX -- the only way to stop is to ctrl-c :p
    data_from_stream = ''
    while 1:
        bytes_read = 0
        allframes = []
        while bytes_read < ONE_KILOBYTE:
            thingthing = stream.read(chunk_size)
            sentstuff = s.send(thingthing)
        #s.sendall(thingread)
            #bytes_read = bytes_read +  sentstuff
            #print "START\n-------------\n" + str(thingread) + "\n-----------------"
            #data_from_stream = data_from_stream + stream.read(chunk_size)
            #bytes_read = bytes_read + 1
        #bytes_read = bytes_read + 1
        #data_from_stream = data_from_stream + stream.read(chunk_size)
        #print str(bytes_read)
        
        #print str(data_from_stream)
        #s.send(bytes(data_from_stream))
        
        #data_from_stream = ""

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
    ip = "127.0.0.1"
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
