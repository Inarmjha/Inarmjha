from chatterbot import ChatBot
import re
import subprocess
import os
from socket import *
import json
from io import StringIO
import ardino
chatbot = ChatBot("Ron Obvious",
storage_adapter='chatterbot.storage.JsonFileStorageAdapter',
logic_adapters=[
      
      "chatterbot.logic.BestMatch",
      "chatterbot.logic.TimeLogicAdapter",
      "chatterbot.logic.MathematicalEvaluation",
      {
        "import_path": "chatterbot.logic.LowConfidenceAdapter",
        "threshold": 0.5,
        "default_response": "I'm so, so, sorry! I cannot understand your strange ramblings..."
      }
    ],)
from chatterbot.trainers import ChatterBotCorpusTrainer
chatbot.set_trainer(ChatterBotCorpusTrainer)
chatbot.train("chatterbot.corpus.english.greetings",
              "chatterbot.corpus.english.conversation",
"chatterbot.corpus.english.emotion", 
"chatterbot.corpus.english.botprofile",
"chatterbot.corpus.english.ai",
"chatterbot.corpus.english.movies")






print("Welcome This is Jha How Can i Help you")
#HOST1 = "192.168.0.2" #local host
#PORT1 = 7002 #open port 7000 for connection 
#s1 = socket(AF_INET, SOCK_STREAM)
#s1.bind((HOST1, PORT1))

while(1):
# The following loop will execute each time the user enters input
       #string=input()
       #how many connections can it receive at one time
        #print the address of the person connected
       #s1.listen(1)
       #conn, addr = s1.accept() #accept the connection
       #print("Connected by: " , addr)
       #data=(str)(conn.recv(1024))
       string=input()
       #lst=re.findall(r'"([^"]*)"',data)
      # inventory=json.loads(data.decode('utf-8'))
       #string=lst[3]
       #string=inventory['messageContent']
       #print(string)
       match=re.search(r'on',string)
       if match:
                    print("Sending thecommand to devices module")              
 #if(ardino.ardinoserver(string)==1):
                    resp="completed the job sir"
               #else:
                    #resp="some error with the device"
       else:
            match1=re.search(r'off',string)
            if match1:
               print("Sending thecommand to devices module")
               if(ardino.ardinoserver(string)==1):
                    resp="completed the job sir"
               else:
                    resp="some error with the device"
            else:
             match2=re.search(r'open',string)
             if match2:
                print("sending the command to device module")
                if(ardino.ardinoserver(string)==1):
                    resp="completed the job sir"
                else:
                    resp="some error with the device"
                
       
             else:
               response = chatbot.get_response(chatbot.input.process_input_statement(string))
               resp=str(response)
               
              # resp = ''.join(resp.split())
             ojosn={}
             
             ojosn['messageType']="MessageFromServer"
             ojosn['messageContent']=resp
             dat_json=json.dumps(ojosn).encode('utf-8')
             #conn.send(dat_json)
              # subprocess.call('espeak '+resp,shell=True)
             print(resp)
       #conn.close()
       #print("closing th conne")      

