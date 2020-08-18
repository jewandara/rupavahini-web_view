import time
import sys
import os
import threading
import json
import datetime

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
               ADD_RE = mdb.add("sent", OID)
               DEL_RE = mdb.deleteBy("wait", OID )
          return RE
     except Exception as error:
          return [0, format(error)]

#################################################################################################
def SEND_DATA_LAYER(jsonArry):
     if '_id' in jsonArry: del jsonArry['_id']
     dl = dataLayer()
     print(jsonArry)
     jsonArrySending = json.dumps(jsonArry)
     print(jsonArrySending)
     #return dl.send(str(jsonArry))
     return dl.send(jsonArrySending)

#################################################################################################
def Reading():
     try: return [ 1, mdb.view("wait", {})]
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
