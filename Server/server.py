import grpc
from concurrent import futures
from google.protobuf import timestamp_pb2

import proto.server_pb2 as server_pb2
import proto.server_pb2_grpc as server_pb2_grpc

from mqtt import MQTTConnection

class Service(server_pb2_grpc.SensorSyncHub):

    def __init__(self):
        self.mqtt_connection = MQTTConnection(topic="test/test", broker="mosquitto", port=1883, on_message=self.handle_mqtt_message)

    def handle_mqtt_message(self, message):
        # Here you can process the received MQTT message and send it to the client
        # Parse the message as needed and create a gRPC response
        # Example: Assuming the message is JSON
        response = server_pb2.DeviceDataResponse(data=message)
        self.stream_response(response)


    # Implement the RPC methods here

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
        # Start streaming the data to the gRPC client
        self.stream_response = context.response_stream.send_message
        # Subscribe to the MQTT topic to receive data
        self.mqtt_connection.subscribe()

        # This function will be continuously running and streaming data to the client
        while not context.is_active():
            pass  # You can add any additional logic here if needed

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
