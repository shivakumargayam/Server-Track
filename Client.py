 #!/usr/bin/env python 

""" 
A simple Server Track  client program
""" 

import socket 
import sys
import math
import datetime

host = 'localhost'

port = 5000
size = 1024
s = None 
try:
    while True:
        s= socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        s.connect((host,port))
        print('connected to server')


        clientCommand=input('Known commands:- <write> <servername> <timestamp in seconds since epoch> <cpu> <ram> OR <read> <servername> <timestamp since epoch secs > <duration of 60mins or 24hrs>') #shiva 1000 25.6 44.2
        #write shiva 1000 1.0 1.0 (Example input for Write opration)
        #read shiva 60/24 3500 (Example input for Read opration)
        print(clientCommand)
        s.send((clientCommand+'\n').encode()) 
        data = s.recv(size) 
        s.close() 
        print ('Your Avarage Load Values or Status:', data)
except Exception as e:
        
    print('exception', e)


