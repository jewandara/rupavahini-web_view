##################################
##      ACCESS DATA LAYER       ##
##################################
import pika
import textfile
import datetime

def rabbitmq(jsonArryData):
    try:
        credentials = pika.PlainCredentials('external_guest', 'apple@2233')
        connection = pika.BlockingConnection(pika.ConnectionParameters('10.62.96.9', 5672, '/', credentials))
        channel = connection.channel()
        #channel.queue_declare(queue='ca_traps', durable=True)
        
        channel.basic_publish(exchange='ca_traps_exchange', routing_key='', body=jsonArryData)
        print("--- (**) RABBITMQ: 'ca_traps' QUEUE")
        connection.close()
        return 1
    except Exception as e:
        connection.close()
        textfile.write_data('--- TABBIT MQ DATA SERVER ERROR FOUND *******')
        textfile.write_data('--- TABBIT MQ DATA SERVER ERROR :'+str(e))
        print (e)
        return 0


def main(snmpArryData):
    #RABBIT_MQ_DATA_LAYER = [ ALARM_ARRY, TYPE_ARRY, DEVICE_ARRY ]
    #['5.60.32.9', 'Huawei AR121', '0994633612_KOTMALE_DIARY_PRODUCTS_PATHANA']
    #['CHASSIS DOWN', 'CRITICAL', "CHASSIS DOWN\n\nSYMPTOMS:\n\nThe chassis and all of its contained blades have stopped responding to polls and/or external requests. Additionally, all devices upstream from them can be contacted implying a chassis fault. A 'Chassis Down' alarm will be generated.\n\nPROBABLE CAUSES:\n\n1) The chassis has been shutdown.\n2) The chassis has lost power.\n3) The network cables connecting the chassis to the network have been removed.\n4) There exists an internal network configuration error on the chassis.\n\nRECOMMENDED ACTIONS:\n\n1) Ensure the chassis has power and is turned on.\n2) Ensure all network cables are connected to the chassis.\n3) Examine the configuration of the chassis and ensure it is correct.\n", 'Fri 18 Oct, 2019 - 17:09:50 - The chassis 0994633612_KOTMALE_DIARY_PRODUCTS_PATHANA and/or one or more of its contained blades have been contacted.\n(event [0x00010f68])\nOnly displaying most recent of 2 event messages.\n']
    #['1', '10/18/2019 17:09:49', '49406', '1', 'NEW', '0x103a2ed', '0x5c20090', 'FALSE', 'TRUE']
    #['0', '10/18/2019 17:05:52', '36676', '3', 'NEW', '0x106b451', '0x5c20090', 'FALSE', 'FALSE']
    if(int(snmpArryData[0][0]) > 0): ALARM_STATUS = "DOWN"
    else: ALARM_STATUS = "UP"
    alarmDate = datetime.datetime.strptime(snmpArryData[0][1], '%m/%d/%Y %H:%M:%S')
    ca_alarm = alarmDate.strftime('%Y-%m-%d %H:%M:%S')
    jsonArry = '{ "caId" : "' + str(snmpArryData[0][2]) + '", "ip" : "' + str(snmpArryData[2][0]) + '", "model" : "' + str(snmpArryData[2][1]) + '", "device" : "' + str(snmpArryData[2][2]) + '", "category" : "' + str(snmpArryData[1][0]) + '", "type" : "' + str(snmpArryData[1][1]) + '", "alarm" : "' + str(ALARM_STATUS) + '", "spTrap" : "' + str(snmpArryData[0][3]) + '", "datetime" : "' + str(ca_alarm) + '" }'
    #print(jsonArry)
    return rabbitmq(jsonArry)

#if __name__ == '__main__':
#    DEVICE_ARRY = ['5.60.32.9', 'Huawei AR121', '0994633612_KOTMALE_DIARY_PRODUCTS_PATHANA']
#    TYPE_ARRY = ['CHASSIS DOWN', 'CRITICAL', "CHASSIS DOWN\n\nSYMPTOMS:\n\nThe chassis and all of its contained blades have stopped responding to polls and/or external requests. Additionally, all devices upstream from them can be contacted implying a chassis fault. A 'Chassis Down' alarm will be generated.\n\nPROBABLE CAUSES:\n\n1) The chassis has been shutdown.\n2) The chassis has lost power.\n3) The network cables connecting the chassis to the network have been removed.\n4) There exists an internal network configuration error on the chassis.\n\nRECOMMENDED ACTIONS:\n\n1) Ensure the chassis has power and is turned on.\n2) Ensure all network cables are connected to the chassis.\n3) Examine the configuration of the chassis and ensure it is correct.\n", 'Fri 18 Oct, 2019 - 17:09:50 - The chassis 0994633612_KOTMALE_DIARY_PRODUCTS_PATHANA and/or one or more of its contained blades have been contacted.\n(event [0x00010f68])\nOnly displaying most recent of 2 event messages.\n']
#    ALARM_ARRY = ['1', '10/18/2019 17:09:49', '49406', '1', 'NEW', '0x103a2ed', '0x5c20090', 'FALSE', 'TRUE']
#    RABBIT_MQ_DATA_LAYER = [ ALARM_ARRY, TYPE_ARRY, DEVICE_ARRY ]
#    main(RABBIT_MQ_DATA_LAYER)




