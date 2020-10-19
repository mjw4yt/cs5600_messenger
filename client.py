#we use these libraries to help us with socket programming
import socket
import threading
import select

#we use this host and port to try and connect to the server.py
HOST = '127.0.0.1'
PORT = 4252

#this function deals with messages and commands
#more commands will be added
def send_handler(s):
    while True:
        #message is whatever we input as a client
        msg = input()
        #if the message is /quit, we exit the client.py
        if msg == "/quit":
            #send message to the 
            s.send("/quit".encode())
            s.shutdown(socket.SHUT_RDWR)
            s.close()
            break
        #if the message is not a command, we send it to the server
        s.send(msg.encode())


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    #connect to that specific host and port
    s.connect((HOST, PORT))
    #if the client sends a message, add that thread to the list of threads
    sender = threading.Thread(target=send_handler, args=(s,))
    sender.start()
    while True:
        if s.fileno() == -1:
            # socket closed
            break
        #this is used for error detection
        r, _, _ = select.select([s], [], [])
        for rs in r:
            if s == rs:
                try:
                    data = rs.recv(1024)
                except OSError:
                    # connection terminated (for some reason)
                    break
                if not data:
                    break
                print(data.decode())
