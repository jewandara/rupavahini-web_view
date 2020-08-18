import time
import sys
import os
import threading
import json
import logging
import datetime
from mysqlDb import mysqlDb
from mongoDb import mongoDb
from dataLayer import dataLayer
db = mysqlDb("alarms_db")
mdb = mongoDb("snmpTraps")


# DEVICE = ['5.100.0.38', 'Cisco 881', '994904998_CEYQUARTZ_MBI_KONGAHAWELA.dialog.lk']
# CATAGORY = ['CHASSIS DOWN', 'CRITICAL', "CHASSIS DOWN\n\nSYMPTOMS:\n\nThe chassis and all of its contained blades have stopped respondiand ensure it is correct.", 'Sat 02 May, 2020 - 18:39:19 - The chassis 994904998_CEYQUARTZ_MBI_KONGAHAWELA.']
# ALARM = ['0', '05/02/2020 18:39:19', '34621', '3', 'NEW', '0x10409d7', '0x21000c', 'FALSE', 'TRUE']

#################################################################################################################################
def Display(TRAPS_DATA):
     sys.stdout.write('FUNCTION '+str(TRAPS_DATA)+'\n')
     sys.stdout.flush()


#################################################################################################
def Sending(DEVICE, CATAGORY, ALARM):
     try:
          if(int(ALARM[0]) > 0): ALARM_STATUS = "DOWN"
          else: ALARM_STATUS = "UP"
          alarmDate = datetime.datetime.strptime(ALARM[1], '%m/%d/%Y %H:%M:%S')
          CA_ALARM_DATE_TIME = alarmDate.strftime('%Y-%m-%d %H:%M:%S')
          jsonArry = '{ "caId" : "' + str(ALARM[2]) + '", "ip" : "' + str(DEVICE[0]) + '", "model" : "' + str(DEVICE[1]) + '", "device" : "' + str(DEVICE[2]) + '", "category" : "' + str(CATAGORY[0]) + '", "type" : "' + str(CATAGORY[1]) + '", "alarm" : "' + str(ALARM_STATUS) + '", "spTrap" : "' + str(ALARM[3]) + '", "datetime" : "' + str(CA_ALARM_DATE_TIME) + '" }'
          #print(jsonArry)
          try:
               dl = dataLayer()
               RE = dl.send(jsonArry)
               if(RE[0]):
                    OUT = mdb.add("sent", json.loads(jsonArry))
                    Display('( ['+str(ALARM[2])+ '] Sending->Sent ) \t: SUCCESS SENDING DATA TO RABBIT MQ DATA SERVER')
               else:
                    OUT = mdb.add("wait", json.loads(jsonArry))
                    Display('( ['+str(ALARM[2])+ '] Sending->Wait ) \t: FAILD SENDING DATA TO RABBIT MQ DATA SERVER *** SAVE DATA TO WAITING LIST')
          except :
               OUT = mdb.add("wait", json.loads(jsonArry))
               Display('( ['+str(ALARM[2])+ '] Sending->Wait ) \t: FAILD SENDING DATA TO RABBIT MQ DATA SERVER *** SAVE DATA TO WAITING LIST')
     except Exception as error:
          Display('( ['+str(ALARM[2])+ '] Saving->Exception ) \t: FAILD SENDING DATA TO RABBIT MQ DATA SERVER AND INSERTING DATA TO WAITING LIST : '+str(format(error)))


#################################################################################################
def Saving(DEVICE, CATAGORY, ALARM):
     try:
          D_DATA = getDevice(DEVICE)[2][0][0]
          C_DATA = getCatagory(CATAGORY)[2][0][0]
          COMMENT_ARRY = ["NEW DOWN ALARM", "NEW UP ALARM", "NO DOWN ALARM", "NO UP ALARM"]
          if(int(ALARM[0]) > 0):
               setDownAlarm(D_DATA, C_DATA, ALARM, COMMENT_ARRY)
               Display('( ['+str(ALARM[2])+ '] Saving->Down ) \t: SUCCESS INSERTING DATA TO MYSQL SERVER')
          else:
               setUpAlarm(D_DATA, C_DATA, ALARM, COMMENT_ARRY)
               Display('( ['+str(ALARM[2])+ '] Saving->Up ) \t: SUCCESS INSERTING DATA TO MYSQL SERVER')
     except Exception as error:
          Display('( ['+str(ALARM[2])+ '] Saving->Exception ) \t: FAILD INSERTING DATA TO MYSQL SERVER : '+str(format(error)))

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

def differentInSecound(date_time):
     TO = datetime.datetime.strptime(str(datetime.datetime.now()), '%Y-%m-%d %H:%M:%S.%f')
     TW = datetime.datetime.strptime(str(date_time), '%Y-%m-%d %H:%M:%S')
     TIME_DIFF = (TO-TW)
     return TIME_DIFF.days * 24 * 3600 + TIME_DIFF.seconds

def sqlString(STR):
     BAD_CHAR = ['"', '`', '--','\n', "'"]
     return ''.join(i for i in str(STR) if not i in BAD_CHAR)

def dts(date_time):
     return datetime.datetime.strptime(date_time, '%m/%d/%Y %H:%M:%S')

def clearAlarm(cid, comment, rid):
     #print('(clearAlarm->Start) : ' + str(comment) + ' - ' + str(datetime.datetime.now()))
     RE = db.edit("alarm_ca_alarms_tb", " `clear`=1, `clear_state`="+str(cid)+", `ca_up_comment`='"+str(comment)+"' ", " `clear`=0 AND `id`="+str(rid)+" ")
     #print('(clearAlarm->Done) : ' + str(RE[1]))
     return RE[0]

def getDevice(device):
     RE = db.view("alarm_ca_devices_tb", " ip = '"+str(device[0])+"' ")
     if (RE[0]): return RE
     else:
          ADD_RE = db.add("alarm_ca_devices_tb( `ip`, `type`, `name` )", " ( '"+str(device[0])+"', '"+str(device[1])+"', '"+sqlString(device[2])+"' )" )
          RE = db.view("alarm_ca_devices_tb", " ip = '"+str(device[0])+"' ")
          return RE

def getCatagory(catagory):
     RE = db.view("alarm_ca_alarm_category_tb", " category = '"+str(catagory[0])+"' ")
     if (RE[0]): return RE
     else:
          ADD_RE = db.add("alarm_ca_alarm_category_tb ( `category`, `status`, `description`, `example` )", " ( '"+str(catagory[0])+"', '"+str(catagory[1])+"', '"+sqlString(catagory[5])+"', '"+sqlString(catagory[6])+"' ) " )
          RE = db.view("alarm_ca_alarm_category_tb", " category = '"+str(catagory[0])+"' ")
          return RE

def checkDownAlarm(did, cid):
     #print('(checkDownAlarm->Start) : WAITTING . . . '+str(datetime.datetime.now()))
     RE = db.viewAll("alarm_ca_alarms_tb", " `did`="+str(did)+" AND `cid`="+str(cid)+" AND `clear`=0 ORDER BY `ca_down_time` DESC ")
     #print('(checkDownAlarm->Done) : ' +str(RE[1]))
     if(RE[2][0]==[]): return [0, []]
     else: return [1, RE[2]]

##################################################################################################
def setDownAlarm(device, catagory, alarm, comment):
     #print('(setDownAlarm->Start) : WAITTING . . . '+str(datetime.datetime.now()))
     OLD_DOWN_ALARMS = checkDownAlarm( device[0], catagory[0] )
     if (OLD_DOWN_ALARMS[0]):
          for row in OLD_DOWN_ALARMS[1][0]:
               clearAlarm(3, comment[3], row[0])
     #print('(setDownAlarm->StartAdding) : NEW DOWN ALARM '+str(datetime.datetime.now()))
     ADD_RE = db.add("alarm_ca_alarms_tb ( `did`, `cid`, `alarmstate`, `mhandle`, `mthandle`, `ackd`, `clearable`, `ca_down_uniq`, `ca_down_specific`, `ca_down_time`, `sql_down_update`, `ca_down_comment` )", " ( "+str(device[0])+", "+str(catagory[0])+", '"+str(alarm[4])+"', '"+str(alarm[5])+"', '"+str(alarm[6])+"', '"+str(alarm[7])+"', '"+str(alarm[8])+"', '"+str(alarm[2])+"', '"+str(alarm[3])+"', '"+str(dts(alarm[1]))+"', now(), '"+str(comment[0])+"' ) " )
     #print('(setDownAlarm->Done) : '+str(ADD_RE[1]))
     return 1

##################################################################################################
def setUpAlarm(device, catagory, alarm, comment):
     #print('(setUpAlarm->start) : WAITTING . . . '+str(datetime.datetime.now()))
     OLD_DOWN_ALARMS = checkDownAlarm( device[0], catagory[0] )
     if(OLD_DOWN_ALARMS[0] == 0):
          #print('(setUpAlarm->checkDownAlarm) : (-) NO DATA FOUND : '+str(datetime.datetime.now()))
          ADD_RE = db.add("alarm_ca_alarms_tb ( `did`, `cid`, `alarmstate`, `mhandle`, `mthandle`, `ackd`, `clearable`, `ca_up_uniq`, `ca_up_specific`, `ca_up_time`, `sql_up_update`, `ca_down_comment`, `ca_up_comment`, `clear`, `clear_state` )", " ( "+str(device[0])+", "+str(catagory[0])+", '"+str(alarm[4])+"', '"+str(alarm[5])+"', '"+str(alarm[6])+"', '"+str(alarm[7])+"', '"+str(alarm[8])+"', '"+str(alarm[2])+"', '"+str(alarm[3])+"', '"+str(dts(alarm[1]))+"', now(), '"+str(comment[2])+"', '"+str(comment[1])+"', 1, 2) " )
          #print('(setUpAlarm->DoneAdding) : '+str(comment[2])+' : '+str(ADD_RE[1]))
     elif(len(OLD_DOWN_ALARMS[1][0]) == 1):
          #print('(setUpAlarm->checkDownAlarm) : (1) ONE DOWN ALARM DATA FOUND : '+str(datetime.datetime.now()))
          PDATE_RE = db.edit("alarm_ca_alarms_tb", " `ca_up_uniq`='"+str(alarm[2])+"', `ca_up_specific`='"+str(alarm[3])+"', `ca_up_time`='"+str(dts(alarm[1]))+"', `sql_up_update`=now(), `ca_up_comment`='"+str(comment[1])+"', `clear`=1, `clear_state`=1 ", " `id`="+str(OLD_DOWN_ALARMS[1][0][0][0])+" ")
          #print('(setUpAlarm->DoneEditing) : '+str(PDATE_RE[1]))
     else:
          #print('(setUpAlarm->checkDownAlarm) : (*) MORE DOWN ALARM DATA FOUND : '+str(datetime.datetime.now()))
          i = len(OLD_DOWN_ALARMS[1][0])
          j = 0
          if(i > 1):
               for row in OLD_DOWN_ALARMS[1][0]:
                    if(i == (j+1)):
                         PDATE_RE = db.edit("alarm_ca_alarms_tb", " `ca_up_uniq`='"+str(alarm[2])+"', `ca_up_specific`='"+str(alarm[3])+"', `ca_up_time`='"+str(dts(alarm[1]))+"', `sql_up_update`=now(), `ca_up_comment`='"+str(comment[1])+"', `clear`=1, `clear_state`=1 ", " `id`="+str(row[0])+" ")
                         #print('(setUpAlarm->DoneEditing) : '+str(PDATE_RE[1]))
                    else: clearAlarm(2, comment[2], row[0])
                    j = j +1
     return 1

##################################################################################################
