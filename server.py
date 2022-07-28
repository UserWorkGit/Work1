from concurrent import futures
import grpc
import logging

import proto_pb2
import proto_pb2_grpc


class Greeter(proto_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        return proto_pb2.HelloReply(message='Hello, %s!' % request.name)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    proto_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('localhost:8080')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()