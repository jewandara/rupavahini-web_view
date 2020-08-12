from pysnmp.carrier.asynsock.dispatch import AsynsockDispatcher
from pysnmp.carrier.asynsock.dgram import udp, udp6
from pyasn1.codec.ber import decoder
from pysnmp.proto import api
import requests
import ipaddress
import os
import server
import textfile
import datalayer

def print_data():
     os.system('cls')
     print('▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀')
     print('▀▀                          _____ __  __   ____                        ▀▀')
     print('▀▀                         |_   _|  \/  |/  ___|                       ▀▀')
     print('▀▀                           | | | \  / |  /                           ▀▀')
     print('▀▀                           | | | |\/| | |                            ▀▀')
     print('▀▀                          _| |_| |  | |  \___                        ▀▀')
     print('▀▀                         |_____|_|  |_|\_____|                       ▀▀')
     print('▀▀                                                                     ▀▀')
     print('▀▀                          -- SIRA VER: 2.0 --                        ▀▀')   
     print('▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀')
     print('▀▀                                                                     ▀▀')
     print('▀▀                     INCIDENT  MONITORING CONSOLE                    ▀▀')
     print('▀▀                                                                     ▀▀')
     print('▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀')
     print('')
     print('--- RUNNING . . .')


def cbFun(transportDispatcher, transportDomain, transportAddress, wholeMsg):
     while wholeMsg:
          print_data()
          #########################################################
          msgVer = int(api.decodeMessageVersion(wholeMsg))
          if msgVer in api.protoModules:
               pMod = api.protoModules[msgVer]
          else:
               textfile.write_data('--- UNSUPPORTED SNMP VERSION %s' % msgVer)
               return
          ##########################################################
          reqMsg, wholeMsg = decoder.decode( wholeMsg, asn1Spec=pMod.Message() )
          reqPDU = pMod.apiMessage.getPDU(reqMsg)
          # CAPTURING IP ADDRESS
          if "10.58.75.103" not in transportAddress: return
          #print('--- From %s:%s ---\n' % (transportDomain, transportAddress) )
          #print('--- From ---\n%s' % (reqPDU) )
          #DEVICE_ARRY = [transportAddress]
          ##########################################################
          # TRANSPORT PROTOCAL
          print('--- 10.58.75.103 . . .')
          if reqPDU.isSameTypeWith(pMod.TrapPDU()):
               if msgVer == api.protoVersion1:
                    #j = pMod.apiTrapPDU.getEnterprise(reqPDU)
                    enterprise_data = pMod.apiTrapPDU.getEnterprise(reqPDU).prettyPrint()
                    agentAddr_data = pMod.apiTrapPDU.getAgentAddr(reqPDU).prettyPrint()
                    genericTrap_data = pMod.apiTrapPDU.getGenericTrap(reqPDU).prettyPrint()
                    specificTrap_data = pMod.apiTrapPDU.getSpecificTrap(reqPDU).prettyPrint()
                    timeStamp_data = pMod.apiTrapPDU.getTimeStamp(reqPDU).prettyPrint()
                    varBinds = pMod.apiTrapPDU.getVarBinds(reqPDU)
               else:
                    varBinds = pMod.apiPDU.getVarBinds(reqPDU)
               #print("---------------------------")
               #print("-", str(enterprise_data))
               #print("-", str(agentAddr_data))
               #print("-", str(genericTrap_data))
               #print("-", str(specificTrap_data))
               #print("-", str(timeStamp_data))
               #print("---------------------------")
                 #specificTrap_data Catagores
                 #-- coldStart trap (0)
                 #-- warmStart trap (1)
                 #-- linkDown trap(2)
                 #-- linkUp trap(3)
                 #-- authenticationFailure trap(4)
                 #-- egpNeighborLoss trap(5)
               ##########################################################
               #print(varBinds)
               print('--- READING . . .')
               ALARM_ARRY_BINARY = []
               ALARM_ARRY_STRING = []
               for oid, val in varBinds:
                    ALARM_ARRY_STRING =  [ str(val) ]+ ALARM_ARRY_STRING 
                    ALARM_ARRY_BINARY =  [ val.prettyPrint()]+ ALARM_ARRY_BINARY 
               ##########################################################
               # ALARM ARRY DATA
               #print(ALARM_ARRY_BINARY)
               #print(ALARM_ARRY_STRING)
               #print ("\n----------------------------------------------------------------------------------\n")
               #print(transportDispatcher)
               #print(wholeMsg)
               #                   IP                      TYPE                    NAME
               DEVICE_ARRY = [ ALARM_ARRY_BINARY[16], ALARM_ARRY_BINARY[15], ALARM_ARRY_BINARY[17] ]
               #                   CAT                     STATUS                  DESCRIPTION                 EXAMPLE
               TYPE_ARRY = [ ALARM_ARRY_BINARY[18], ALARM_ARRY_BINARY[19], ALARM_ARRY_STRING[13], ALARM_ARRY_STRING[12] ]
               #                   STATUS                  DAT & TIME                  UNIQ ID             GENERIC TRAP            ALARM STATE             MHA                 MTHA                      ACKD              CLEARABLE   
               ALARM_ARRY = [ ALARM_ARRY_BINARY[0],  ALARM_ARRY_BINARY[14], str(transportAddress[1]), str(specificTrap_data), ALARM_ARRY_STRING[3], ALARM_ARRY_STRING[6], ALARM_ARRY_STRING[5], ALARM_ARRY_STRING[2], ALARM_ARRY_STRING[1] ]

               print("-------------------------------------------------------------------------")
               if(server.main(ALARM_ARRY, TYPE_ARRY, DEVICE_ARRY)):
                    textfile.write_data('--- NEW RECODE UPDATED SUCCESS IN MYSQL SERVER')
                    print("--- NEW RECODE UPDATED SUCCESS IN MYSQL SERVER")
                    print("-------------------------------------------------------------------------")
               else:
                    textfile.write_data('--- RECODE UPDATED ERROR FOUND IN MYSQL SERVER')
                    print("--- RECODE UPDATED ERROR FOUND IN MYSQL SERVER")
                    print("-------------------------------------------------------------------------")
               RABBIT_MQ_DATA_LAYER = [ ALARM_ARRY, TYPE_ARRY, DEVICE_ARRY ]
               if(datalayer.main(RABBIT_MQ_DATA_LAYER)):
                    textfile.write_data('--- NEW RECODE UPDATED SUCCESS IN RABBIT MQ DATA SERVER')
                    print("--- NEW RECODE UPDATED SUCCESS IN RABBIT MQ DATA SERVER")
                    print("-------------------------------------------------------------------------")
               else:
                    textfile.write_data('--- RECODE UPDATED ERROR FOUND IN RABBIT MQ DATA SERVER')
                    print("--- RECODE UPDATED ERROR FOUND IN RABBIT MQ DATA SERVER")
                    print("-------------------------------------------------------------------------")
               print("")
               print(DEVICE_ARRY)
               print("")
               print(TYPE_ARRY)
               print("")
               print("")
               print(ALARM_ARRY)
               print("")
               print("")
               print('▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀')     
          return wholeMsg


def main():
     transportDispatcher = AsynsockDispatcher()
     transportDispatcher.registerRecvCbFun(cbFun)
     transportDispatcher.registerTransport( udp.domainName, udp.UdpSocketTransport().openServerMode(('0.0.0.0', 162)) )
     transportDispatcher.registerTransport( udp6.domainName, udp6.Udp6SocketTransport().openServerMode(('::1', 162)) )
     transportDispatcher.jobStarted(1)
     while True:
          try:
               transportDispatcher.runDispatcher()
          except Exception as e:
               textfile.write_data('--- SNMP ERROR FOUND *******')
               textfile.write_data('--- SNMP ERROR :'+str(e))
               print (e)
          else:
               break

