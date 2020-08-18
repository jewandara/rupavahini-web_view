import time
import sys
import os
import threading
import logging
import datetime
import json

SCRIPT_PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_PATH+'/scripts/')
sys.path.insert(0, SCRIPT_PATH+'/libs/')

from mongoDb import mongoDb
from dataLayer import dataLayer
mdb = mongoDb("snmpTraps")
from bson.objectid import ObjectId

#################################################################################################
def Sending(jsonArry):
     try:
          ID = jsonArry['_id']
          RE = SEND_DATA_LAYER(jsonArry)
          if(RE[0]):
               OID = {"_id": ObjectId(ID)}
               ADD_RE = mdb.add("sent", jsonArry)
               DEL_RE = mdb.deleteBy("wait", OID )
          return RE
     except Exception as error:
          return [0, format(error)]

#################################################################################################
def SEND_DATA_LAYER(jsonArry):
     if '_id' in jsonArry: del jsonArry['_id']
     dl = dataLayer()
     #print(jsonArry)
     jsonArrySending = json.dumps(jsonArry)
     #print(jsonArrySending)
     #return dl.send(str(jsonArry))
     return dl.send(jsonArrySending)

#################################################################################################
def Reading():
     try: return [ 1, mdb.view('wait', {})]
     except Exception as error: return [ 0 , format(error)]

##################################################################################################
def writting(DATA):
     try:
          REPORT_DATE = str(datetime.datetime.now().date())
          ABSOLUTE_PATH = os.path.dirname(os.path.abspath(__file__))
          FILE = ABSOLUTE_PATH + "\logs\LOG_"+REPORT_DATE+".log"
          with open(FILE,"a+") as dataFile:
               now_date_time = datetime.datetime.now()
               dataFile.write( str(now_date_time)+"\t:  "+DATA+"\r\n")
          return [ 1, DATA ]
     except Exception as error: return [ 0 , format(error)]

##################################################################################################
def Display(TRAPS_DATA):
     sys.stdout.write('RESENDER '+str(TRAPS_DATA)+'\n')
     sys.stdout.flush()

##################################################################################################
def Resender():
     try:
          RE = Reading()
          for trapsInJson in RE[1][2]:
               if(trapsInJson):
                    SEND_RE = Sending(trapsInJson)
                    Display('( [***] Resender->Sending ) : SUCCESS SENDING DATA TO DATALAYER : '+str(SEND_RE[1]))
                    #print(trapsInJson)
     except Exception as ERROR:
          Display('( [***] Resender->Exception ) : RESENDER FUNCTION THREAD HAS A EXCEPTION')

#################################################################################################################################
#################################################################################################################################
def Main():
     while True:
          now = datetime.datetime.now()
          if( (now.minute==00 or now.minute==15 or now.minute==30 or now.minute==46) and now.second==00):
               try: Resender()
               except Exception as ERROR: Display('( [***] Main->Exception ) : MAIN FUNCTION START RUNNING IN A THREAD EXCEPTION : '+ str(format(error))) 

#################################################################################################################################
if __name__ == '__main__':
     MainThread = threading.Thread(target=Main())
     MainThread.start()
