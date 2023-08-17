# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import server.server_pb2 as server__pb2


class ServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetDevice = channel.unary_unary(
                '/sensor_sync_hub.Service/GetDevice',
                request_serializer=server__pb2.GetDeviceRequest.SerializeToString,
                response_deserializer=server__pb2.Device.FromString,
                )
        self.GetDevices = channel.unary_unary(
                '/sensor_sync_hub.Service/GetDevices',
                request_serializer=server__pb2.Empty.SerializeToString,
                response_deserializer=server__pb2.Devices.FromString,
                )
        self.GetSensors = channel.unary_unary(
                '/sensor_sync_hub.Service/GetSensors',
                request_serializer=server__pb2.Empty.SerializeToString,
                response_deserializer=server__pb2.Sensors.FromString,
                )
        self.GetDeviceData = channel.unary_unary(
                '/sensor_sync_hub.Service/GetDeviceData',
                request_serializer=server__pb2.GetDeviceDataRequest.SerializeToString,
                response_deserializer=server__pb2.DataList.FromString,
                )
        self.GetSensorData = channel.unary_unary(
                '/sensor_sync_hub.Service/GetSensorData',
                request_serializer=server__pb2.GetSensorDataRequest.SerializeToString,
                response_deserializer=server__pb2.DataList.FromString,
                )
        self.StreamDeviceData = channel.unary_stream(
                '/sensor_sync_hub.Service/StreamDeviceData',
                request_serializer=server__pb2.GetDeviceDataRequest.SerializeToString,
                response_deserializer=server__pb2.Data.FromString,
                )
        self.StreamSensorData = channel.unary_stream(
                '/sensor_sync_hub.Service/StreamSensorData',
                request_serializer=server__pb2.GetSensorDataRequest.SerializeToString,
                response_deserializer=server__pb2.Data.FromString,
                )
        self.DeleteDevice = channel.unary_unary(
                '/sensor_sync_hub.Service/DeleteDevice',
                request_serializer=server__pb2.DeleteRequest.SerializeToString,
                response_deserializer=server__pb2.Empty.FromString,
                )
        self.DeleteData = channel.unary_unary(
                '/sensor_sync_hub.Service/DeleteData',
                request_serializer=server__pb2.DeleteRequest.SerializeToString,
                response_deserializer=server__pb2.Empty.FromString,
                )
        self.DeleteSensor = channel.unary_unary(
                '/sensor_sync_hub.Service/DeleteSensor',
                request_serializer=server__pb2.DeleteRequest.SerializeToString,
                response_deserializer=server__pb2.Empty.FromString,
                )


class ServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetDevice(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetDevices(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetSensors(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetDeviceData(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetSensorData(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StreamDeviceData(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StreamSensorData(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteDevice(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteData(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteSensor(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetDevice': grpc.unary_unary_rpc_method_handler(
                    servicer.GetDevice,
                    request_deserializer=server__pb2.GetDeviceRequest.FromString,
                    response_serializer=server__pb2.Device.SerializeToString,
            ),
            'GetDevices': grpc.unary_unary_rpc_method_handler(
                    servicer.GetDevices,
                    request_deserializer=server__pb2.Empty.FromString,
                    response_serializer=server__pb2.Devices.SerializeToString,
            ),
            'GetSensors': grpc.unary_unary_rpc_method_handler(
                    servicer.GetSensors,
                    request_deserializer=server__pb2.Empty.FromString,
                    response_serializer=server__pb2.Sensors.SerializeToString,
            ),
            'GetDeviceData': grpc.unary_unary_rpc_method_handler(
                    servicer.GetDeviceData,
                    request_deserializer=server__pb2.GetDeviceDataRequest.FromString,
                    response_serializer=server__pb2.DataList.SerializeToString,
            ),
            'GetSensorData': grpc.unary_unary_rpc_method_handler(
                    servicer.GetSensorData,
                    request_deserializer=server__pb2.GetSensorDataRequest.FromString,
                    response_serializer=server__pb2.DataList.SerializeToString,
            ),
            'StreamDeviceData': grpc.unary_stream_rpc_method_handler(
                    servicer.StreamDeviceData,
                    request_deserializer=server__pb2.GetDeviceDataRequest.FromString,
                    response_serializer=server__pb2.Data.SerializeToString,
            ),
            'StreamSensorData': grpc.unary_stream_rpc_method_handler(
                    servicer.StreamSensorData,
                    request_deserializer=server__pb2.GetSensorDataRequest.FromString,
                    response_serializer=server__pb2.Data.SerializeToString,
            ),
            'DeleteDevice': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteDevice,
                    request_deserializer=server__pb2.DeleteRequest.FromString,
                    response_serializer=server__pb2.Empty.SerializeToString,
            ),
            'DeleteData': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteData,
                    request_deserializer=server__pb2.DeleteRequest.FromString,
                    response_serializer=server__pb2.Empty.SerializeToString,
            ),
            'DeleteSensor': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteSensor,
                    request_deserializer=server__pb2.DeleteRequest.FromString,
                    response_serializer=server__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'sensor_sync_hub.Service', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Service(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetDevice(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sensor_sync_hub.Service/GetDevice',
            server__pb2.GetDeviceRequest.SerializeToString,
            server__pb2.Device.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetDevices(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sensor_sync_hub.Service/GetDevices',
            server__pb2.Empty.SerializeToString,
            server__pb2.Devices.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetSensors(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sensor_sync_hub.Service/GetSensors',
            server__pb2.Empty.SerializeToString,
            server__pb2.Sensors.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetDeviceData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sensor_sync_hub.Service/GetDeviceData',
            server__pb2.GetDeviceDataRequest.SerializeToString,
            server__pb2.DataList.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetSensorData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sensor_sync_hub.Service/GetSensorData',
            server__pb2.GetSensorDataRequest.SerializeToString,
            server__pb2.DataList.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StreamDeviceData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/sensor_sync_hub.Service/StreamDeviceData',
            server__pb2.GetDeviceDataRequest.SerializeToString,
            server__pb2.Data.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StreamSensorData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/sensor_sync_hub.Service/StreamSensorData',
            server__pb2.GetSensorDataRequest.SerializeToString,
            server__pb2.Data.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteDevice(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sensor_sync_hub.Service/DeleteDevice',
            server__pb2.DeleteRequest.SerializeToString,
            server__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sensor_sync_hub.Service/DeleteData',
            server__pb2.DeleteRequest.SerializeToString,
            server__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteSensor(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sensor_sync_hub.Service/DeleteSensor',
            server__pb2.DeleteRequest.SerializeToString,
            server__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
