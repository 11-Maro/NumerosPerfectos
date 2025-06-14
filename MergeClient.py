import socket
import MergeSort

HOST = '192.168.1.1'
PORT = 50007
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

# Receives arraystring in chunks
arraystring = ''
print('Receiving data...')
while True:
    data = s.recv(4096).decode()  # Receives data in chunks and decodes to string
    arraystring += data  # Adds data to array string
    if ']' in data:  # When end of data is received
        break

array = eval(arraystring)
print('Data received, sorting array...')

# Sorts the array which it is allocated
array = MergeSort.mergesort(array)
print('Array sorted, sending data...')

# Converts array into string to be sent back to server
arraystring = repr(array).encode()  # Encodes string to bytes for sending
s.sendall(arraystring)  # Sends array string
print('Data sent.')

s.close()
