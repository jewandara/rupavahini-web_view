##########################################################################################
#################################### Version 0.0.1 #######################################
##########################################################################################
##########################################################################################
#############################   DATA FINDING FUNCTION  ###################################
##--------------------------------------------------------------------------------------##
##                                   threshold = > value                                ##
##--------------------------------------------------------------------------------------##
##      Alarm Catagory                                     Clear Alarm Values(Minits)   ##
##--------------------------------------------------------------------------------------##
##--A critical threshold violation has occurred.                    34533 MINITS        ##  
##--A major threshold violation has occurred.                       34533 MINITS        ##  
##--A minor threshold violation has occurred.                       34533 MINITS        ##  
##--AUTHENTICATION FAILURE TRAP RECEIVED                            34533 MINITS        ##  
##--BAD LINK DETECTED                                               34533 MINITS        ##  
##--BLADE STATUS UNKNOWN                                            34533 MINITS        ##  
##--CRITICAL ALARM ON INTERFACE DUE TO LOST BGP PEERING SESSION     34533 MINITS        ##  
##--DEVICE HAS REBOOTED                                             34533 MINITS        ##  
##--DEVICE HAS STOPPED RESPONDING TO POLLS                          34533 MINITS        ##  
##--DIFFERENT TYPE MODEL                                            34533 MINITS        ##  
##--HIGH AGGREGATE CPU UTILIZATION                                  34533 MINITS        ##  
##--HIGH AGGREGATE MEMORY UTILIZATION                               34533 MINITS        ##  
##--HIGH CPU USAGE                                                  34533 MINITS        ##  
##--HIGH CPU USAGE                                                  34533 MINITS        ##  
##--HIGH CPU UTILIZATION                                            34533 MINITS        ##  
##--HIGH MEMORY UTILIZATION                                         34533 MINITS        ##  
##--MANAGEMENT AGENT LOST                                           34533 MINITS        ##  
##--MINOR ALARM ON INTERFACE DUE TO LOST BGP PEERING SESSION        34533 MINITS        ##  
##--ONECLICK SERVER LOGS DIRECTORY THRESHOLD EXCEEDED               34533 MINITS        ##  
##--------------------------------------------------------------------------------------##
##########################################################################################
##########   DATA FINDING FUNCTION  ############
##--------------------------------------------##
##           threshold = > specific           ##
##--------------------------------------------##
##    Specific Trap              Values       ##
##  -- coldStart                trap (0)      ##
##  -- warmStart                trap (1)      ##
##  -- linkDown                 trap(2)       ##
##  -- linkUp                   trap(3)       ##
##  -- authenticationFailure    trap(4)       ##
##  -- egpNeighborLoss          trap(5)       ##
###-------------------------------------------##
################################################
import os
import textfile
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
import datetime


##################################################################################################
def sql_connector(query):
    try:
        os.environ['NO_PROXY'] = 'localhost'
        RE = []
        connection = mysql.connector.connect(host="localhost", user="user_alarm", passwd="UserAlarm#365", database="alarms_db")
        dbcursor = connection.cursor()
        dbcursor.execute(query)
        RE = dbcursor.fetchall()
    except mysql.connector.Error as error :
        connection.rollback()
        textfile.write_data("--- Failed inserting record into python_users table {}")
    finally:
        textfile.write_data("--- NEW QUERY : "+str(query))
        del dbcursor
        connection.close()
    return RE


##################################################################################################
def diff_second(date_time):
    TO = datetime.datetime.strptime(str(datetime.datetime.now()), '%Y-%m-%d %H:%M:%S.%f')
    TW = datetime.datetime.strptime(str(date_time), '%Y-%m-%d %H:%M:%S')
    TIME_DIFF = (TO-TW)
    return TIME_DIFF.days * 24 * 3600 + TIME_DIFF.seconds

def sql_query(STR):
    BAD_CHAR = ['"', '`', '--','\n', "'"]
    return ''.join(i for i in str(STR) if not i in BAD_CHAR)

def dts(date_time):
    return datetime.datetime.strptime(date_time, '%m/%d/%Y %H:%M:%S')


##################################################################################################      
def get_database_device(device):
    row = sql_connector("SELECT * FROM alarm_ca_devices_tb WHERE ip = '"+str(device[0])+"' ")
    if (row == []) or (row == None):
        #print("INSERT INTO alarm_ca_devices_tb ( `ip`, `type`, `name` ) VALUES ( '"+str(device[0])+"', '"+str(device[1])+"', '"+sql_query(device[2])+"' ) ")
        sql_connector("INSERT INTO alarm_ca_devices_tb ( `ip`, `type`, `name` ) VALUES ( '"+str(device[0])+"', '"+str(device[1])+"', '"+sql_query(device[2])+"' ) ")
        row = sql_connector("SELECT * FROM alarm_ca_devices_tb WHERE ip = '"+str(device[0])+"' ")
    return (row)
def get_database_catagory(catagory):
    row = sql_connector("SELECT * FROM alarm_ca_alarm_category_tb WHERE category = '"+str(catagory[0])+"' ")
    if (row == []) or (row == None):
        #print("INSERT INTO alarm_ca_alarm_category_tb ( `category`, `status`, `description`, `example` ) VALUES ( '"+str(catagory[0])+"', '"+str(catagory[1])+"', '"+sql_query(catagory[2])+"', '"+sql_query(catagory[3])+"' ) ")
        sql_connector("INSERT INTO alarm_ca_alarm_category_tb ( `category`, `status`, `description`, `example` ) VALUES ( '"+str(catagory[0])+"', '"+str(catagory[1])+"', '"+sql_query(catagory[2])+"', '"+sql_query(catagory[3])+"' ) ")
        row = sql_connector("SELECT * FROM alarm_ca_alarm_category_tb WHERE category = '"+str(catagory[0])+"' ")
    return (row)


##################################################################################################
def clear_alarm(cid, comment, rid):
    sql_connector("UPDATE `alarm_ca_alarms_tb` SET `clear`=1, `clear_state`="+str(cid)+", `ca_up_comment`='"+str(comment)+"' WHERE `clear`=0 AND `id`="+str(rid)+" ")
    return 1


##################################################################################################
#                   STATUS                  DAT & TIME                  UNIQ ID             GENERIC TRAP            ALARM STATE             MHA                 MTHA                      ACKD              CLEARABLE   
# ALARM_ARRY = [ ALARM_ARRY_BINARY[0],  ALARM_ARRY_BINARY[14], str(transportAddress[1]), str(specificTrap_data), ALARM_ARRY_STRING[3], ALARM_ARRY_STRING[6], ALARM_ARRY_STRING[5], ALARM_ARRY_STRING[2], ALARM_ARRY_STRING[1] ]
##################################################################################################  
##############################################################################################
###  UNDER THRESHOLD                                                                        ##
##   ---------------------------------------------------------------------------------------##
##   5 = ALARM CLEARED UNDER THRESHOLD                                                      ##
##   6 = ALARM CLEARED UNDER BREACHED THRESHOLD                                             ##
##   7 = ALARM CLEARED WITHOUT DOWN ALARM UNDER BREACHED THRESHOLD (CREATE NEW ALARM)       ##
##   8 = ALARM CLEARED WITHOUT UP ALARM UNDER BREACHED THRESHOLD                            ##
##   9 = ALARM CLEARED WITHOUT UP ALARM UNDER THRESHOLD                                     ##
##   10 = ALARM CLEARED NEW DOWN ALARM UNDER BREACHED THRESHOLD                             ##
##   11 = ALARM CLEARED NEW DOWN ALARM UNDER THRESHOLD                                      ##
##                                                                                          ##
##   BY DEFAULT                                                                             ##
##   ---------------------------------------------------------------------------------------##
##   0 = NEW DOWN ALARM                                                                     ##
##   1 = ALARM CLEARED BY DEFAULT                                                           ##
##   2 = ALARM CLEARED WITHOUT DOWN ALARM BY DEFAULT (CREATE NEW ALARM)                     ##
##   3 = ALARM CLEARED WITHOUT UP ALARM BY DEFAULT                                          ##
##   4 = ALARM CLEARED NEW DOWN ALARM BY DEFAULT                                            ##
##############################################################################################
def main(ALARM_ARRY, TYPE_ARRY, DEVICE_ARRY):
    D_DATA = get_database_device(DEVICE_ARRY)[0]
    C_DATA = get_database_catagory(TYPE_ARRY)[0]
    COMMENT_ARRY = ["NEW DOWN ALARM", "ALARM CLEARED BY DEFAULT", "ALARM CLEARED WITHOUT DOWN ALARM BY DEFAULT", "ALARM CLEARED WITHOUT UP ALARM BY DEFAULT", "ALARM CLEARED NEW DOWN ALARM BY DEFAULT", "ALARM CLEARED UNDER THRESHOLD", "ALARM CLEARED UNDER BREACHED THRESHOLD", "ALARM CLEARED WITHOUT DOWN ALARM UNDER BREACHED THRESHOLD", "ALARM CLEARED WITHOUT UP ALARM UNDER BREACHED THRESHOLD", "ALARM CLEARED WITHOUT UP ALARM UNDER THRESHOLD", "ALARM CLEARED NEW DOWN ALARM UNDER BREACHED THRESHOLD", "ALARM CLEARED NEW DOWN ALARM UNDER THRESHOLD"]
    print("--- IMS SERVER TIME : %s" % str(datetime.datetime.now()))
    if(int(ALARM_ARRY[0]) > 0):
        DOWN_DATA = set_alarm_down(D_DATA, C_DATA, ALARM_ARRY, COMMENT_ARRY)
        print("--- (**) DOWN ALARM ")
    else:
        UP_DATA = set_alarm_up(D_DATA, C_DATA, ALARM_ARRY, COMMENT_ARRY)
        print("--- (**) UP ALARM ")
    return 1

























##################################################################################################
#RESULT = check_database_alarm_up( 64, 3, 1)
#print(RESULT)
#if RESULT == []: print("NO DATA")
#else:
#    for xy in RESULT:
#        for x in xy:
#            print(x)
##################################################################################################
def check_database_alarm_up(did, cid, limit):
    if (limit): limit_string = " LIMIT 1 "
    else: limit_string = " "
    sql_query = "SELECT * FROM alarm_ca_alarms_tb WHERE `did`="+str(did)+" AND `cid`="+str(cid)+" AND `clear`=0 AND `ca_up_time` IS NULL ORDER BY `ca_down_time` DESC "+limit_string
    #sql_query_0 = "SELECT * FROM alarm_ca_alarms_tb WHERE `did`="+str(did)+" AND `cid`="+str(cid)+" AND `ca_down_specific`= 0 AND `clear`=0 AND `ca_up_time` IS NULL ORDER BY `ca_down_time` DESC "+limit_string
    #sql_query_1 = "SELECT * FROM alarm_ca_alarms_tb WHERE `did`="+str(did)+" AND `cid`="+str(cid)+" AND `ca_down_specific`= 1 AND `clear`=0 AND `ca_up_time` IS NULL ORDER BY `ca_down_time` DESC "+limit_string
    #sql_query_2 = "SELECT * FROM alarm_ca_alarms_tb WHERE `did`="+str(did)+" AND `cid`="+str(cid)+" AND `ca_down_specific`= 2 AND `clear`=0 AND `ca_up_time` IS NULL ORDER BY `ca_down_time` DESC "+limit_string
    #sql_query_3 = "SELECT * FROM alarm_ca_alarms_tb WHERE `did`="+str(did)+" AND `cid`="+str(cid)+" AND `ca_down_specific`= 3 AND `clear`=0 AND `ca_up_time` IS NULL ORDER BY `ca_down_time` DESC "+limit_string
    #sql_query_4 = "SELECT * FROM alarm_ca_alarms_tb WHERE `did`="+str(did)+" AND `cid`="+str(cid)+" AND `ca_down_specific`= 4 AND `clear`=0 AND `ca_up_time` IS NULL ORDER BY `ca_down_time` DESC "+limit_string
    #sql_query_5 = "SELECT * FROM alarm_ca_alarms_tb WHERE `did`="+str(did)+" AND `cid`="+str(cid)+" AND `ca_down_specific`= 5 AND `clear`=0 AND `ca_up_time` IS NULL ORDER BY `ca_down_time` DESC "+limit_string
    #row = [sql_connector(sql_query_0), sql_connector(sql_query_1), sql_connector(sql_query_2), sql_connector(sql_query_3), sql_connector(sql_query_4), sql_connector(sql_query_5)]
    row = [sql_connector(sql_query)]
    RESULT = []
    if row != []:
        for tt in row:
            for rx in tt:
                if (rx != []):
                    if RESULT == []: RESULT = rx
                    else: RESULT = [rx, RESULT]
    return (RESULT)







##################################################################################################
#RESULT = check_database_alarm_down(1, 64, 3, 3, '2019-05-23 00:00:00', 1)
#print(RESULT)
#if RESULT == []: print("NO DATA")
#else:
#    for xy in RESULT:
#        for x in xy:
#            print(x)
##################################################################################################
def check_database_alarm_down( threshold, did, cid, specific, time, limit ):
    if(limit):
        if (threshold):
            sql_query = "SELECT * FROM alarm_ca_alarms_tb WHERE `did`="+str(did)+" AND `cid`="+str(cid)+" AND `clear`=0 AND `ca_down_specific`="+str(specific)+" AND (`ca_down_time` = STR_TO_DATE('"+str(time)+"','%m/%d/%Y %H:%i:%s')) ORDER BY `ca_down_time` DESC LIMIT 1 "
        else:
            sql_query = "SELECT * FROM alarm_ca_alarms_tb WHERE `did`="+str(did)+" AND `cid`="+str(cid)+" AND `clear`=0 AND (`ca_down_time` = STR_TO_DATE('"+str(time)+"','%m/%d/%Y %H:%i:%s')) ORDER BY `ca_down_time` DESC LIMIT 1 "
    else:
        if (threshold):
            sql_query = "SELECT * FROM alarm_ca_alarms_tb WHERE `did`="+str(did)+" AND `cid`="+str(cid)+" AND `clear`=0 AND `ca_down_specific`="+str(specific)+" AND (`ca_down_time` != STR_TO_DATE('"+str(time)+"','%m/%d/%Y %H:%i:%s')) ORDER BY `ca_down_time` DESC "
        else:
            sql_query = "SELECT * FROM alarm_ca_alarms_tb WHERE `did`="+str(did)+" AND `cid`="+str(cid)+" AND `clear`=0 AND (`ca_down_time` != STR_TO_DATE('"+str(time)+"','%m/%d/%Y %H:%i:%s')) ORDER BY `ca_down_time` DESC "
    return sql_connector(sql_query)














##################################################################################################
def set_alarm_down(device, catagory, alarm, comment):
    RESULT_ONE_ROW = check_database_alarm_down( catagory[5], device[0], catagory[0], alarm[3], alarm[1], 1 )
    if RESULT_ONE_ROW == []:
        ###-------------------------------------------------------------------------------------###
        ### 0 = NEW DOWN ALARM                                                                  ###
        ###-------------------------------------------------------------------------------------###
        sql_connector("INSERT INTO alarm_ca_alarms_tb ( `did`, `cid`, `alarmstate`, `mhandle`, `mthandle`, `ackd`, `clearable`, `ca_down_uniq`, `ca_down_specific`, `ca_down_time`, `sql_down_update`, `ca_down_comment` ) VALUES ( "+str(device[0])+", "+str(catagory[0])+", '"+str(alarm[4])+"', '"+str(alarm[5])+"', '"+str(alarm[6])+"', '"+str(alarm[7])+"', '"+str(alarm[8])+"', '"+str(alarm[2])+"', '"+str(alarm[3])+"', '"+str(dts(alarm[1]))+"', now(), '"+str(comment[0])+"' ) ")
        RESULT_ONE_ROW = check_database_alarm_down( catagory[5], device[0], catagory[0], alarm[3], alarm[1], 1 )
    RESULT_MULTI_ROW = check_database_alarm_down( catagory[5], device[0], catagory[0], alarm[3], alarm[1], 0 ) 
    if RESULT_MULTI_ROW != []:
        for row in RESULT_MULTI_ROW:
            if(int(catagory[4])):
                if(diff_second(row[10])>catagory[3]):
                    ###-------------------------------------------------------------------------------------###
                    ### 10 = ALARM CLEARED NEW DOWN ALARM UNDER BREACHED THRESHOLD                          ###
                    ###-------------------------------------------------------------------------------------###
                    clear_alarm(10, comment[10], row[0])
                else:
                    ###-------------------------------------------------------------------------------------###
                    ### 11 = ALARM CLEARED NEW DOWN ALARM UNDER THRESHOLD                                   ###
                    ###-------------------------------------------------------------------------------------###
                    clear_alarm(11, comment[11], row[0])
            else:
                ###-------------------------------------------------------------------------------------###
                ### 4 = ALARM CLEARED NEW DOWN ALARM BY DEFAULT                                         ###
                ###-------------------------------------------------------------------------------------###
                clear_alarm(4, comment[4], row[0])
    return 1






##################################################################################################
def set_alarm_up(device, catagory, alarm, comment):
    RESULT_ONE_ROW = check_database_alarm_up( device[0], catagory[0], 1 )
    if RESULT_ONE_ROW == []:
        ###-------------------------------------------------------------------------------------###
        ### 2 = ALARM CLEARED WITHOUT DOWN ALARM BY DEFAULT (CREATE NEW ALARM)                  ###
        ###-------------------------------------------------------------------------------------###
        sql_connector("INSERT INTO alarm_ca_alarms_tb ( `did`, `cid`, `alarmstate`, `mhandle`, `mthandle`, `ackd`, `clearable`, `ca_up_uniq`, `ca_up_specific`, `ca_up_time`, `sql_up_update`, `ca_up_comment`, `clear`, `clear_state` ) VALUES ( "+str(device[0])+", "+str(catagory[0])+", '"+str(alarm[4])+"', '"+str(alarm[5])+"', '"+str(alarm[6])+"', '"+str(alarm[7])+"', '"+str(alarm[8])+"', '"+str(alarm[2])+"', '"+str(alarm[3])+"', '"+str(dts(alarm[1]))+"', now(), '"+str(comment[2])+"', 1, 2) ")
    else:
        ONE_RECORD = 1 ## ADD ONLE NEW ONE CLEAR RECORD FOR ALL (5) FIVE CATAGORIES IN Specific Trap DATA
        row = RESULT_ONE_ROW
        if(int(catagory[4])):
            if(diff_second(row[10])>catagory[3]):
                ###-------------------------------------------------------------------------------------###
                ### 6 = ALARM CLEARED UNDER BREACHED THRESHOLD                                          ###
                ###-------------------------------------------------------------------------------------###
                clear_alarm(6, comment[6], row[0])
                ###-------------------------------------------------------------------------------------###
                ### 7 = ALARM CLEARED WITHOUT DOWN ALARM UNDER BREACHED THRESHOLD (CREATE NEW ALARM)    ###
                ###-------------------------------------------------------------------------------------###
                if (ONE_RECORD):
                    sql_connector("INSERT INTO alarm_ca_alarms_tb ( `did`, `cid`, `alarmstate`, `mhandle`, `mthandle`, `ackd`, `clearable`, `ca_up_uniq`, `ca_up_specific`, `ca_up_time`, `sql_up_update`, `ca_up_comment`, `clear`, `clear_state` ) VALUES ( "+str(device[0])+", "+str(catagory[0])+", '"+str(alarm[4])+"', '"+str(alarm[5])+"', '"+str(alarm[6])+"', '"+str(alarm[7])+"', '"+str(alarm[8])+"', '"+str(alarm[2])+"', '"+str(alarm[3])+"', '"+str(dts(alarm[1]))+"', now(), '"+str(comment[7])+"', 1, 7) ")
                    ONE_RECORD = 0
            else:
                ###-------------------------------------------------------------------------------------##
                ### 5 = ALARM CLEARED UNDER THRESHOLD                                                   ##
                ###-------------------------------------------------------------------------------------##
                sql_connector("UPDATE `alarm_ca_alarms_tb` SET `ca_up_uniq`='"+str(alarm[2])+"', `ca_up_specific`='"+str(alarm[3])+"', `ca_up_time`='"+str(dts(alarm[1]))+"', `sql_up_update`=now(), `ca_up_comment`='"+str(comment[5])+"', `clear`=1, `clear_state`=5  WHERE `clear`=0 AND `id`="+str(row[0])+" ")
        else:
            ###-------------------------------------------------------------------------------------###
            ### 1 = ALARM CLEARED BY DEFAULT                                                        ###
            ###-------------------------------------------------------------------------------------###
            sql_connector("UPDATE `alarm_ca_alarms_tb` SET `ca_up_uniq`='"+str(alarm[2])+"', `ca_up_specific`='"+str(alarm[3])+"', `ca_up_time`='"+str(dts(alarm[1]))+"', `sql_up_update`=now(), `ca_up_comment`='"+str(comment[1])+"', `clear`=1, `clear_state`=1  WHERE `clear`=0 AND `id`="+str(row[0])+" ")
    RESULT_MULTI_ROW = check_database_alarm_up( device[0], catagory[0], 0 )
    if RESULT_MULTI_ROW != []:
        if(catagory[4]):
            for row in RESULT_MULTI_ROW:
                if(diff_second(row[10])>catagory[3]):
                    ###-------------------------------------------------------------------------------------###
                    ### 8 = ALARM CLEARED WITHOUT UP ALARM UNDER BREACHED THRESHOLD                         ###
                    ###-------------------------------------------------------------------------------------###
                    clear_alarm(8, comment[8], row[0])
                else:
                    ###-------------------------------------------------------------------------------------###
                    ### 9 = ALARM CLEARED WITHOUT UP ALARM UNDER THRESHOLD                                  ###
                    ###-------------------------------------------------------------------------------------###
                    clear_alarm(9, comment[9], row[0])
        else:
            ###-------------------------------------------------------------------------------------###
            ### 1 = ALARM CLEARED BY DEFAULT                                                        ###
            ###-------------------------------------------------------------------------------------###
            clear_alarm(1, comment[1], row[0])
    return 1






