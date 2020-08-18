import time
import sys
import os
import threading
import logging
import datetime

SCRIPT_PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_PATH+'/scripts/')
sys.path.insert(0, SCRIPT_PATH+'/libs/')

from pysnmp.carrier.asynsock.dispatch import AsynsockDispatcher
from pysnmp.carrier.asynsock.dgram import udp, udp6
from pyasn1.codec.ber import decoder
from pysnmp.proto import api
import func




#################################################################################################################################
def Display(TRAPS_DATA):
     sys.stdout.write('RECEIVIN '+str(TRAPS_DATA)+'\n')
     sys.stdout.flush()


def Main():
     transportDispatcher = AsynsockDispatcher()
     transportDispatcher.registerRecvCbFun(Reciver)
     transportDispatcher.registerTransport( udp.domainName, udp.UdpSocketTransport().openServerMode(('0.0.0.0', 162)) )
     transportDispatcher.registerTransport( udp6.domainName, udp6.Udp6SocketTransport().openServerMode(('::1', 162)) )
     transportDispatcher.jobStarted(1)
     while True:
          try:
               #logging.info('(Main) : MAIN FUNCTION START RUNNING IN A THREAD')
               ReciverThread = threading.Thread(target=transportDispatcher.runDispatcher())
               ReciverThread.start()
          except Exception as ERROR:
               #logging.info('(Main->Exception) : MAIN FUNCTION START RUNNING IN A THREAD EXCEPTION : '+str(ERROR))
               Display('( [***] Main->Exception ) : MAIN FUNCTION START RUNNING IN A THREAD EXCEPTION') 
          else: break


def Reciver(transportDispatcher, transportDomain, transportAddress, wholeMsg):
     while wholeMsg:
          try:
               #logging.info('(Main) : MAIN FUNCTION START RUNNING IN A THREAD')
               MessageThread = threading.Thread(target=Message, args=(transportDispatcher, transportDomain, transportAddress, wholeMsg))
               MessageThread.start()
          except Exception as ERROR:
               #logging.info('(Reciver->Exception) : RECIVER FUNCTION START READING WHOLE MESSAGE IN A THREAD EXCEPTION : '+str(ERROR))
               Display('( [***] Reciver->Exception ) : RECIVER FUNCTION START RECIVING DATA IN A THREAD EXCEPTION :'+str(ERROR)) 
          else: break
          return wholeMsg


def Message(transportDispatcher, transportDomain, transportAddress, wholeMsg):
     try:
          #logging.info('(Reciver) : RECIVER FUNCTION START READING WHOLE MESSAGE IN A THREAD')
          msgVer = int(api.decodeMessageVersion(wholeMsg))
          if msgVer in api.protoModules: pMod = api.protoModules[msgVer]
          else:
               #logging.info('(Reciver->Error) : UNSUPPORTED SNMP VERSION : %s' % msgVer)
               Display('( [***] Message->Error ) : UNSUPPORTED SNMP VERSION : %s' % msgVer)
               return
          #------------------------------------------------------------------------------
          reqMsg, wholeMsg = decoder.decode( wholeMsg, asn1Spec=pMod.Message() )
          reqPDU = pMod.apiMessage.getPDU(reqMsg)
          if "10.58.75.103" not in transportAddress: return
          if reqPDU.isSameTypeWith(pMod.TrapPDU()):
               if msgVer == api.protoVersion1:
                    enterprise_data = pMod.apiTrapPDU.getEnterprise(reqPDU).prettyPrint()
                    agentAddr_data = pMod.apiTrapPDU.getAgentAddr(reqPDU).prettyPrint()
                    genericTrap_data = pMod.apiTrapPDU.getGenericTrap(reqPDU).prettyPrint()
                    specificTrap_data = pMod.apiTrapPDU.getSpecificTrap(reqPDU).prettyPrint()
                    timeStamp_data = pMod.apiTrapPDU.getTimeStamp(reqPDU).prettyPrint()
                    varBinds = pMod.apiTrapPDU.getVarBinds(reqPDU)
               else:
                    varBinds = pMod.apiPDU.getVarBinds(reqPDU)
          #------------------------------------------------------------------------------
               ALARM_ARRY_BINARY = []
               ALARM_ARRY_STRING = []
               for oid, val in varBinds:
                    ALARM_ARRY_STRING =  [ str(val) ]+ ALARM_ARRY_STRING
                    ALARM_ARRY_BINARY =  [ val.prettyPrint()]+ ALARM_ARRY_BINARY
          #------------------------------------------------------------------------------
               #                   IP                      TYPE                    NAME
               DEVICE_ARRY = [ ALARM_ARRY_BINARY[16], ALARM_ARRY_BINARY[15], ALARM_ARRY_BINARY[17] ]
               #                   CAT                     STATUS                  DESCRIPTION                 EXAMPLE
               CATAGORY_ARRY = [ ALARM_ARRY_BINARY[18], ALARM_ARRY_BINARY[19], ALARM_ARRY_STRING[13], ALARM_ARRY_STRING[12] ]
               #                   STATUS                  DAT & TIME                  UNIQ ID             GENERIC TRAP            ALARM STATE             MHA                 MTHA                      ACKD              CLEARABLE  
               ALARM_ARRY = [ ALARM_ARRY_BINARY[0],  ALARM_ARRY_BINARY[14], str(transportAddress[1]), str(specificTrap_data), ALARM_ARRY_STRING[3], ALARM_ARRY_STRING[6], ALARM_ARRY_STRING[5], ALARM_ARRY_STRING[2], ALARM_ARRY_STRING[1] ]

               Display('( ['+str(ALARM_ARRY[2])+ '] Message->Alarm ) \t: '+str(ALARM_ARRY[0])+' : '+str(ALARM_ARRY[1])+' : '+str(DEVICE_ARRY[0])+'['+str(DEVICE_ARRY[1]).upper()+'] : '+str(CATAGORY_ARRY[0]).upper()+'['+str(CATAGORY_ARRY[1]).upper()+'] ' )
          #------------------------------------------------------------------------------
               #SqlSave = threading.Thread(target=func.Saving, args=(DEVICE_ARRY, CATAGORY_ARRY, ALARM_ARRY))
               #SqlSave.start()
               #RE = func.Saving()
               #if(RE[0]):
                    #logging.info('(Reciver->Saving:MySqlDatabase) : SUCCESS INSERTING DATA TO MYSQL SERVER')
                    #Display('( ['+str(ALARM_ARRY[2])+ '] Message->Saving ) : SUCCESS INSERTING DATA TO MYSQL SERVER')
                    #logging.info('(Reciver->Display) : SUCCESS INSERTING DATA TO MYSQL SERVER')
               #else:
                    #logging.info('(Reciver->Saving:MySqlError)) : ERROR INSERTING DATA TO MYSQL SERVER')
                    #Display('( ['+str(ALARM_ARRY[2])+ '] Message->Saving ) : ERROR INSERTING DATA TO MYSQL SERVER : ' + str(RE[1][1]))
                    #logging.info('(Reciver->Display) : ERROR INSERTING DATA TO MYSQL SERVER')
          #------------------------------------------------------------------------------
               RabbitMqSend = threading.Thread(target=func.Sending, args=(DEVICE_ARRY, CATAGORY_ARRY, ALARM_ARRY))
               RabbitMqSend.start()
               #RE = func.Sending(DEVICE_ARRY, CATAGORY_ARRY, ALARM_ARRY)
               #if(RE[0]):
                    #logging.info('(Reciver->Sending:RabbitMqServer) : SUCCESS SENDING DATA TO RABBIT MQ DATA SERVER')
                    #Display('( ['+str(ALARM_ARRY[2])+ '] Message->Sending ) : SUCCESS SENDING DATA TO RABBIT MQ DATA SERVER')
                    #logging.info('(Reciver->Display) : SUCCESS SENDING DATA TO RABBIT MQ DATA SERVER')
               #else:
                    #logging.info('(Reciver->Sending:RabbitMqDataLayerError)) : ERROR INSERTING DATA TO MYSQL SERVER')
                    #Display('( ['+str(ALARM_ARRY[2])+ '] Message->Sending ) : ERROR SENDING DATA TO RABBIT MQ DATA SERVER : ' + str(RE[1][1]))
                    #logging.info('(Reciver->Display) : ERROR INSERTING DATA TO MYSQL SERVER')
          #------------------------------------------------------------------------------ 
               #Display('(Device_Data) : '+str(DEVICE_ARRY))
               #Display('(Category_Data) : '+str(CATAGORY_ARRY))
               #Display('(Alar_mData) : '+str(ALARM_ARRY))
     except :
          #logging.info('(Reciver->Exception) : RECIVER FUNCTION START READING WHOLE MESSAGE IN A THREAD EXCEPTION : '+str(ERROR))
          Display('( [***] Message->Exception ) : MESSAGE FUNCTION START READING WHOLE MESSAGE IN A THREAD EXCEPTION') 

#################################################################################################################################
if __name__ == '__main__':
     #format = "%(asctime)s: %(message)s"
     #logging.basicConfig(format=format, level=logging.INFO, datefmt="%Y-%m-%d %H:%M:%S")
     #logging.info(" - starting main thread.")
     MainThread = threading.Thread(target=Main())
     MainThread.start()
