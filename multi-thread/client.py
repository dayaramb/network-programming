#!/usr/bin/python
import threading, socket,sys

try: 
  c=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  c.connect(('localhost',5300))
  
except socket.error, (value,message):
    if c:
      c.close()
    print "Couldnot open the socket", message
    sys.exit(1)


while True:
  data= raw_input("Enter data to send:")   
  if data=='q' or data=='Q':
     c.send(data)
     break
  c.send(data)
  print "Received data:", c.recv(1024)



  
