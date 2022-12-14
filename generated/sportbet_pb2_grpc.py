# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import generated.sportbet_pb2 as sportbet__pb2


class SportBetManagementServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateBet = channel.unary_unary(
                '/SportBetManagementService/CreateBet',
                request_serializer=sportbet__pb2.CreateBetRequest.SerializeToString,
                response_deserializer=sportbet__pb2.CreateBetResponse.FromString,
                )
        self.ReadBet = channel.unary_unary(
                '/SportBetManagementService/ReadBet',
                request_serializer=sportbet__pb2.ReadBetRequest.SerializeToString,
                response_deserializer=sportbet__pb2.ReadBetResponse.FromString,
                )
        self.UpdateBet = channel.unary_unary(
                '/SportBetManagementService/UpdateBet',
                request_serializer=sportbet__pb2.UpdateBetRequest.SerializeToString,
                response_deserializer=sportbet__pb2.UpdateBetResponse.FromString,
                )
        self.DeleteBet = channel.unary_unary(
                '/SportBetManagementService/DeleteBet',
                request_serializer=sportbet__pb2.DeleteBetRequest.SerializeToString,
                response_deserializer=sportbet__pb2.DeleteBetResponse.FromString,
                )


class SportBetManagementServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateBet(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReadBet(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateBet(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteBet(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SportBetManagementServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateBet': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateBet,
                    request_deserializer=sportbet__pb2.CreateBetRequest.FromString,
                    response_serializer=sportbet__pb2.CreateBetResponse.SerializeToString,
            ),
            'ReadBet': grpc.unary_unary_rpc_method_handler(
                    servicer.ReadBet,
                    request_deserializer=sportbet__pb2.ReadBetRequest.FromString,
                    response_serializer=sportbet__pb2.ReadBetResponse.SerializeToString,
            ),
            'UpdateBet': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateBet,
                    request_deserializer=sportbet__pb2.UpdateBetRequest.FromString,
                    response_serializer=sportbet__pb2.UpdateBetResponse.SerializeToString,
            ),
            'DeleteBet': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteBet,
                    request_deserializer=sportbet__pb2.DeleteBetRequest.FromString,
                    response_serializer=sportbet__pb2.DeleteBetResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'SportBetManagementService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SportBetManagementService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateBet(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SportBetManagementService/CreateBet',
            sportbet__pb2.CreateBetRequest.SerializeToString,
            sportbet__pb2.CreateBetResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReadBet(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SportBetManagementService/ReadBet',
            sportbet__pb2.ReadBetRequest.SerializeToString,
            sportbet__pb2.ReadBetResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateBet(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SportBetManagementService/UpdateBet',
            sportbet__pb2.UpdateBetRequest.SerializeToString,
            sportbet__pb2.UpdateBetResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteBet(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SportBetManagementService/DeleteBet',
            sportbet__pb2.DeleteBetRequest.SerializeToString,
            sportbet__pb2.DeleteBetResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
