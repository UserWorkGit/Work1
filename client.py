import grpc

import proto_pb2
import proto_pb2_grpc


def run():
    print("Press 'Enter' to exit")
    name = input("Enter the name of the author or the title of the book: ")
    while len(name) != 0:
        with grpc.insecure_channel('localhost:8080') as channel:
            stub = proto_pb2_grpc.GreeterStub(channel)
            response = stub.Library(proto_pb2.Request(name=name))
            print()
            if response.message[0] == '0':
                print('There is no such book or author in the database.')
            if response.message[0] == '1':
                array_books = response.message[2:].split()
                print(name + ":")
                for name_book in array_books:
                    print(name_book)
            if response.message[0] == '2':
                print(response.message[2:] + ":")
                print(name)
        print()
        print("Press 'Enter' to exit")
        name = input("Enter the name of the author or the title of the book: ")


run()
