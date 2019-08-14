import socket
import struct
import math

s = socket.socket()

port = 5842
host = 'vortex.labs.overthewire.org'

s.connect((host, port))
print("Retrieving data ....")
data = s.recv(1024)
print(data)

var = struct.unpack_from('<IIII',data,0)
print("Here you go!")
print(var)

acc = sum(var)
print(acc)
ret = struct.pack('I',acc)

s.send(ret)
data2 = s.recv(1024)
print(data2)
s.close()
