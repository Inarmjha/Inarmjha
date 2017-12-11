from socket import *
import subprocess
HOST = "192.168.0.3" #local host
PORT = 7004 #open port 7000 for connection
s = socket(AF_INET, SOCK_STREAM)
s.bind((HOST, PORT))
subprocess.call('espeak goodmoarningSirthisisjha',shell=True)
#subprocess.call('python ./cv/facerecognition.py',shell=True)
s.listen(1) #how many connections can it receive at one time
conn, addr = s.accept() #accept the connection
print "Connected by: " , addr #print the address of the person connected


while(True):
    
     conn.sendall(raw_input())
     conn.close()
     
     
         
print("connection closed")


