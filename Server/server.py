import grpc
from concurrent import futures
from google.protobuf import timestamp_pb2

import proto.server_pb2 as server_pb2
import proto.server_pb2_grpc as server_pb2_grpc

from mqtt import MQTTConnection

import random
import string

class Service(server_pb2_grpc.SensorSyncHub):

    def __init__(self):
        self.mqtt_connection = MQTTConnection(topic="test/test", broker="mosquitto", port=1883, on_message=self.handle_mqtt_message)

    def handle_mqtt_message(self, message):
        print(message)

        # Here you can process the received MQTT message and send it to the client
        # Parse the message as needed and create a gRPC response
        # Example: Assuming the message is JSON
        response = server_pb2.Data(value=2)

    def GetDevice(self, request, context):
        pass

    def GetDevices(self, request, context):
        pass

    def GetSensors(self, request, context):
        pass

    def GetDeviceData(self, request, context):
        pass

    def GetSensorData(self, request, context):
        pass

    def StreamDeviceData(self, request, context):
        characters = string.ascii_letters + string.digits    
        client_id = ''.join(random.choice(characters) for _ in range(10))

        device_connection = MQTTConnection(topic="test/test", 
                                           broker="mosquitto", 
                                           port=1883, 
                                           on_message=self.handle_device_message,
                                           client_id=client_id)

        while context._state.client != 'cancelled' :
            pass  # You can add any additional logic here if needed
        device_connection.client.disconnect()

    def handle_device_message(self, message):
        print("New message: " + message)
        response = server_pb2.Data(value=0.6)
        yield response  

    def StreamSensorData(self, request, context):
        pass

    def DeleteDevice(self, request, context):
        pass

    def DeleteData(self, request, context):
        pass

    def DeleteSensor(self, request, context):
        pass

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    server_pb2_grpc.add_SensorSyncHubServicer_to_server(Service(), server)
    server.add_insecure_port('[::]:8000')  # Change the port as needed
    server.start()
    print("Sensor Sync Hub service started on port 8000")
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
