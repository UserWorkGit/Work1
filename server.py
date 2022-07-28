from concurrent import futures
import grpc
import logging
import proto_pb2
import proto_pb2_grpc
import pymysql
from config import localhost, password, port, user, db_name


class Greeter(proto_pb2_grpc.GreeterServicer):
    def Library(self, request, context):
        con = pymysql.connect(
            host=localhost,
            port=port,
            user=user,
            password=password,
            database=db_name,
            cursorclass=pymysql.cursors.DictCursor
        )
        # name_arr is array names autor or books.
        # The first digit is responsible for what is returned.
        # 0 - nothing, 1 - books, 2 - the author.
        name_arr = '1'
        try:
            with con.cursor() as cursor:
                select_all_rows = "SELECT * FROM books"
                cursor.execute(select_all_rows)
                rows = cursor.fetchall()
                for row in rows:
                    if row['Book'] == request.name:
                        name_arr = '2'
                        name_arr = name_arr + ' ' + row['Autors ']
                    if row['Autors'] == request.name:
                        name_arr = name_arr + ' ' + row['Book']
                if len(name_arr) == 1:
                    name_arr = '0'
        finally:
            con.close()
        return proto_pb2.Reply(message=name_arr)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    proto_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('localhost:8080')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
