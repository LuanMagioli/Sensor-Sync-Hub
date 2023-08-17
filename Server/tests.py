import grpc
from concurrent import futures
import time
import paho.mqtt.client as mqtt
from google.protobuf.timestamp_pb2 import Timestamp

# Import the generated gRPC client module
import server.server_pb2 as server_pb2
import server.server_pb2_grpc as server_pb2_grpc

# gRPC server address
GRPC_SERVER_ADDRESS = 'localhost:8000'

# MQTT broker settings
MQTT_BROKER_ADDRESS = 'mosquitto'
MQTT_BROKER_PORT = 1883

def mqtt_on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker with result code "+str(rc))

def simulate_data_publish(client, device_id, sensor_id, value):
    topic = f"device/{device_id}/sensor/{sensor_id}"
    client.publish(topic, f"{value}")

def run_grpc_tests():
    # Create a gRPC channel to the server
    channel = grpc.insecure_channel(GRPC_SERVER_ADDRESS)
    stub = server_pb2_grpc.ServiceStub(channel)

    # Perform gRPC operations here
    # Example: Get devices
    devices_response = stub.GetDevices(server_pb2.Empty())
    print("Devices:", devices_response.devices)

    # Example: Get device data
    device_data_response = stub.GetDeviceData(server_pb2.GetDeviceDataRequest(device_id='device_id_here'))
    print("Device Data:", device_data_response.data)

    # Example: Stream device data
    stream_request = server_pb2.GetDeviceDataRequest(device_id='device_id_here')
    stream = stub.StreamDeviceData(stream_request)
    for data in stream:
        print("Streamed Data:", data)

def main():
    # Run the gRPC tests
    run_grpc_tests()

    # Simulate sending data through MQTT
    mqtt_client = mqtt.Client()
    mqtt_client.on_connect = mqtt_on_connect
    mqtt_client.connect(MQTT_BROKER_ADDRESS, MQTT_BROKER_PORT, 60)
    mqtt_client.loop_start()

    # Simulate sending data for different devices and sensors
    while True:
        simulate_data_publish(mqtt_client, 'device1', 'sensor1', 25.0)
        simulate_data_publish(mqtt_client, 'device2', 'sensor2', 30.0)
        simulate_data_publish(mqtt_client, 'device3', 'sensor3', 35.0)
        time.sleep(5)

if __name__ == '__main__':
    main()
