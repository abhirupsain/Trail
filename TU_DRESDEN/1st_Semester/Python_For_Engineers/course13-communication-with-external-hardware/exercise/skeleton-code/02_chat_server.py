"""
rudimentary chat application (server part)

"""

# based on source: http://docs.python.org/library/socket.html#example


import socket

HOST = ""                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
s = socket.socket()
s.settimeout(30)          # 30 seconds timeout (for s.listen())
s.bind((HOST, PORT))
print("Server started.\nWaiting for connection with client\n")
s.listen(1)
conn, addr = s.accept()
conn.settimeout(30)
print("Connected by", addr)
while 1:
    data = conn.recv(1024)
    if not data:
        break  # if client connection terminated => data=""

    print("Message from client:", data)
    print("Input response:")
    response = input()

    # convert unicode string to byte array with utf8 encoding
    bin_msg = bytes(response, "utf8")
    conn.send(bin_msg)

conn.close()
print("Server: Connection closed.")


