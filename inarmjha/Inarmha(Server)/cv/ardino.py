from socket import *
import subprocess
import json

def ardinoserver(string):
    HOST = "192.168.0.6" #local host
    PORT = 5000 #open port 7000 for connection
    s = socket(AF_INET, SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(1) #how many connections can it receive at one time
    conn, addr = s.accept() #accept the connection
    print("Connected by: " , addr) #print the address of the person connected


     
    
     #conn.sendall(str)
    
    conn.send(string.encode('utf-8'))
    #data=conn.recv(1024)
    data="yes"
    print(data)
    if(str(data)=="yes"):
          conn.close()
          return 1
    else :
          conn.close()
          return 0 
    
    
