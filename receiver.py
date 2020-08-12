################################
##      RECV DATA LAYER       ##
################################
import pika

credentials = pika.PlainCredentials('external_guest', 'apple@2233')
connection = pika.BlockingConnection(pika.ConnectionParameters('10.62.96.9', 5672, '/', credentials))
channel = connection.channel()
channel.queue_declare(queue='ca_traps', durable=True)

def callbackdunc(ch, meth, properties, text):
    print(text)


channel.basic_consume('ca_traps', callbackdunc, auto_ack=True)
print("Waitting . . .")
channel.start_consuming()

#def basic_consume(self, queue, on_message_callback, auto_ack=False, exclusive=False, consumer_tag=None, arguments=None):
