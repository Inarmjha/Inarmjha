from socket import *
import subprocess
import base64
import json
import cv2
import re
def datareceive(s):
    
     subprocess.call('espeak goodmoarningSirthisisjha',shell=True)
     s.listen(1) #how many connections can it receive at one time
     conn, addr = s.accept() #accept the connection
     print("Connected by: " , addr) #print the address of the person connected


     
     data=conn.recv(1024)
     print(data)
     match=re.search(r'open',data)
     if match:
           ojson={}
           ojson['messageType']="MessageFromServer"
           ojson['messageContent']="opening the gate"
           json_d=json.dumps(ojson)
           conn.send(json_d)
           print("sending the dataaa")
     else:
           conn.send("storing for future use!!!!!")
     conn.close() 
     
     print("connection closed")

def  datasend(str,s,frame):
     subprocess.call('espeak Iamauthenticating',shell=True)
     #subprocess.call('python ./cv/facerecognition.py',shell=True)
     s.listen(1) #how many connections can it receive at one time
     conn, addr = s.accept() #accept the connection
     print("Connected by: " , addr) #print the address of the person connected


     
    
     #conn.sendall(str)
     outjson={}
     encode_param=[int(cv2.IMWRITE_JPEG_QUALITY),90]
     result, imgencode = cv2.imencode('.jpg', frame, encode_param)
     encoded_string = base64.b64encode(imgencode)
     outjson['img']=encoded_string
     outjson['id']=str
     json_data=json.dumps(outjson)
     conn.send(json_data)
     
     conn.close()
     
     
         
     print("connection closed")
def sendbind():
    HOST = "192.168.0.102" #local host
    PORT = 7004 #open port 7000 for connection
    s = socket(AF_INET, SOCK_STREAM)
    s.bind((HOST, PORT))
    return s

def receivebind():
     HOST1 = "192.168.0.102" #local host
     PORT1 = 7002 #open port 7000 for connection 
     s1 = socket(AF_INET, SOCK_STREAM)
     s1.bind((HOST1, PORT1))
     return s1
