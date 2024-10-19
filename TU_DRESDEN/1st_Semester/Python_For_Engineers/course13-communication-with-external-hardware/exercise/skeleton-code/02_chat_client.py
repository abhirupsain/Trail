"""
rudimentary chat application (client part)

"""

# based on source: http://docs.python.org/library/socket.html#example


import socket

def send(msg):
    # send and print
    # use `s` from global namespace

    # convert unicode string to byte array (with utf8 encoding)
    bin_msg = bytes(msg, "utf8")
    XXX()  # send the data
    print("sent data:", bin_msg)

def receive():
    XXX = XXX(XXX)
    print("message from server", repr(XXX))

HOST = 'localhost'        # The 'remote' host
PORT = 50007              # The same port as used by the server
s = socket.socket()
s.connect((HOST, PORT))

send("Hello, World")
receive()
print("answer:")
send(input())
receive()

send("")  # send empty string -> server shuts itself down
s.close()
print("client: connection closed.")

