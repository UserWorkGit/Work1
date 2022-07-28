import grpc

import proto_pb2
import proto_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:8080') as channel:
        stub = proto_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(proto_pb2.HelloRequest(name='Boris'))
        print("Greeter client received: " + response.message)


run()
