#################################################################
######################## Sira Version 2.0.1 #####################
#################################################################

import pika
import datetime

class __rabbitmq:
    def __init__(self, serverName='10.62.96.9', serverPort=5672, serverUser='external_guest', serverPass='apple@2233', channelExchange='ca_traps_exchange', channelRoutingKey='ca_traps'):
    #def __init__(self, serverName='10.62.96.9', serverPort=5672, serverUser='external_guest', serverPass='apple@2233', channelExchange='caSnmpTraps_exchange', channelRoutingKey='SnmpTraps'):
        self.server_name = serverName
        self.server_port = serverPort
        self.server_user = serverUser
        self.server_pass = serverPass
        self.server_channel_exchange = channelExchange
        self.server_channel_routing_key = channelRoutingKey
    ####################################
    def _send(self, json_arry_data):
        try:
            credentials = pika.PlainCredentials(self.server_user, self.server_pass)
            connection = pika.BlockingConnection(pika.ConnectionParameters(self.server_name, self.server_port, '/', credentials))
            channel = connection.channel()
            #channel.queue_declare(queue='ca_traps', durable=True)
            channel.basic_publish(exchange=self.server_channel_exchange, routing_key=self.server_channel_routing_key, body=json_arry_data)
            connection.close()
            return [1, 'SENDING DATA TO DATA LAYER SUCCESSFULLY (_send)', str(json_arry_data) ]
        except Exception as error:
            connection.close()
            return [0, 'EXCEPTION AND FAILED SENDING DATA TO DATA LAYER (_send)', format(error)]


class dataLayer(__rabbitmq):
    def send(self, data): return self._send(data) 

#################################################################
######################## Sira Version 2.0.1 #####################
#################################################################
#-------------------------------------------
#-------------------------------------------
#db = dataLayer()
#x = db.send("")
#print(x)

#################################################################
