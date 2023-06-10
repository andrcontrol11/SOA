# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import mafia_pb2 as mafia__pb2


class SoaMafiaServerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.RegistratePlayer = channel.unary_unary(
                '/SoaMafiaServer/RegistratePlayer',
                request_serializer=mafia__pb2.Player.SerializeToString,
                response_deserializer=mafia__pb2.PlayersList.FromString,
                )
        self.NotificationStream = channel.unary_stream(
                '/SoaMafiaServer/NotificationStream',
                request_serializer=mafia__pb2.Player.SerializeToString,
                response_deserializer=mafia__pb2.Notifications.FromString,
                )
        self.Disconnect = channel.unary_unary(
                '/SoaMafiaServer/Disconnect',
                request_serializer=mafia__pb2.Player.SerializeToString,
                response_deserializer=mafia__pb2.Empty.FromString,
                )
        self.StartGame = channel.unary_unary(
                '/SoaMafiaServer/StartGame',
                request_serializer=mafia__pb2.Player.SerializeToString,
                response_deserializer=mafia__pb2.StartGameResponse.FromString,
                )
        self.Ready = channel.unary_unary(
                '/SoaMafiaServer/Ready',
                request_serializer=mafia__pb2.Player.SerializeToString,
                response_deserializer=mafia__pb2.Empty.FromString,
                )
        self.SendVote = channel.unary_unary(
                '/SoaMafiaServer/SendVote',
                request_serializer=mafia__pb2.Vote.SerializeToString,
                response_deserializer=mafia__pb2.VoteResponse.FromString,
                )
        self.MafiaChoice = channel.unary_unary(
                '/SoaMafiaServer/MafiaChoice',
                request_serializer=mafia__pb2.Vote.SerializeToString,
                response_deserializer=mafia__pb2.VoteResponse.FromString,
                )
        self.CommissionerChoice = channel.unary_unary(
                '/SoaMafiaServer/CommissionerChoice',
                request_serializer=mafia__pb2.Vote.SerializeToString,
                response_deserializer=mafia__pb2.VoteResponse.FromString,
                )


class SoaMafiaServerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def RegistratePlayer(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def NotificationStream(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Disconnect(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StartGame(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Ready(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendVote(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MafiaChoice(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CommissionerChoice(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SoaMafiaServerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'RegistratePlayer': grpc.unary_unary_rpc_method_handler(
                    servicer.RegistratePlayer,
                    request_deserializer=mafia__pb2.Player.FromString,
                    response_serializer=mafia__pb2.PlayersList.SerializeToString,
            ),
            'NotificationStream': grpc.unary_stream_rpc_method_handler(
                    servicer.NotificationStream,
                    request_deserializer=mafia__pb2.Player.FromString,
                    response_serializer=mafia__pb2.Notifications.SerializeToString,
            ),
            'Disconnect': grpc.unary_unary_rpc_method_handler(
                    servicer.Disconnect,
                    request_deserializer=mafia__pb2.Player.FromString,
                    response_serializer=mafia__pb2.Empty.SerializeToString,
            ),
            'StartGame': grpc.unary_unary_rpc_method_handler(
                    servicer.StartGame,
                    request_deserializer=mafia__pb2.Player.FromString,
                    response_serializer=mafia__pb2.StartGameResponse.SerializeToString,
            ),
            'Ready': grpc.unary_unary_rpc_method_handler(
                    servicer.Ready,
                    request_deserializer=mafia__pb2.Player.FromString,
                    response_serializer=mafia__pb2.Empty.SerializeToString,
            ),
            'SendVote': grpc.unary_unary_rpc_method_handler(
                    servicer.SendVote,
                    request_deserializer=mafia__pb2.Vote.FromString,
                    response_serializer=mafia__pb2.VoteResponse.SerializeToString,
            ),
            'MafiaChoice': grpc.unary_unary_rpc_method_handler(
                    servicer.MafiaChoice,
                    request_deserializer=mafia__pb2.Vote.FromString,
                    response_serializer=mafia__pb2.VoteResponse.SerializeToString,
            ),
            'CommissionerChoice': grpc.unary_unary_rpc_method_handler(
                    servicer.CommissionerChoice,
                    request_deserializer=mafia__pb2.Vote.FromString,
                    response_serializer=mafia__pb2.VoteResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'SoaMafiaServer', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SoaMafiaServer(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def RegistratePlayer(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SoaMafiaServer/RegistratePlayer',
            mafia__pb2.Player.SerializeToString,
            mafia__pb2.PlayersList.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def NotificationStream(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/SoaMafiaServer/NotificationStream',
            mafia__pb2.Player.SerializeToString,
            mafia__pb2.Notifications.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Disconnect(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SoaMafiaServer/Disconnect',
            mafia__pb2.Player.SerializeToString,
            mafia__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StartGame(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SoaMafiaServer/StartGame',
            mafia__pb2.Player.SerializeToString,
            mafia__pb2.StartGameResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Ready(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SoaMafiaServer/Ready',
            mafia__pb2.Player.SerializeToString,
            mafia__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SendVote(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SoaMafiaServer/SendVote',
            mafia__pb2.Vote.SerializeToString,
            mafia__pb2.VoteResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def MafiaChoice(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SoaMafiaServer/MafiaChoice',
            mafia__pb2.Vote.SerializeToString,
            mafia__pb2.VoteResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CommissionerChoice(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SoaMafiaServer/CommissionerChoice',
            mafia__pb2.Vote.SerializeToString,
            mafia__pb2.VoteResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
