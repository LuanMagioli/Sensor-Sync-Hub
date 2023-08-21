from paho.mqtt import client as mqtt
from threading import Thread

class MQTTConnection():
    """
    A simple MQTT client that connects to a broker, subscribe to an topic and publishes a message
    
    :param str topic: The topic to subscribe/publish to (default: "python/mqtt")
    :param str broker: The url of the broker (default: "mosquitto")
    :param int port: The port of the broker (default: 1883)
    :param function on_message: A function that will be called when a message is received, if doesn't set, no thread will be started (default: None)
    """
        
    def __init__(self, topic = "python/mqtt", broker = 'mosquitto', port = 1883, on_message = None , client_id = "device-manager"):
        self.client = mqtt.Client(client_id) 
        self.topic = topic
        
        def on_connect(client, userdata, flags, rc):
            if rc == 0:
                client.subscribe(topic)
                print(f"Connected to topic \"{topic}\" on {broker}:{port}")
            else:
                print(f"Failed to connect to topic \"{topic}\" on {broker}:{port}")
                raise Exception("Failed to connect to MQTT Broker, return code %d\n", result)

        #Define on_connect event Handler

        if(on_message != None):
            def on_msg(client, userdata, message):
                    on_message(str(message.payload.decode("utf-8")))
            self.client.on_message = on_msg

        
        self.client.on_connect = on_connect

        #Connect to MQTT Broker
        self.client.connect_async(broker, port)
        self.client.loop_start()
    
    def subscribe(self):
        """
        A fupynction that subscribes to the topic
        """
        self.client.subscribe(self.topic)

    
    def publish(self, message):
        """
        A function that publishes a message to the topic
        
        :param str message: The message to publish
        :param str topic: The topic to publish to (default: self.topic)
        """
        
        result = self.client.publish(self.topic, message)
        if result[0] == 0:
            print(f"Send \"{message}\" to topic: {self.topic}")
        else:
            print(f"Failed to send message to topic: {self.topic}")