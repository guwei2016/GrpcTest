import grpc
from example import data_pb2, data_pb2_grpc

_HOST = 'localhost'
_PORT = '8080'

def run():
    conn = grpc.insecure_channel(_HOST + ':' + _PORT)
    client = data_pb2_grpc.FormatDataStub(channel=conn)
    text1 = 'hello,world!'
    response = client.DoFormat(data_pb2.Data(text=text1))
    print("received: " + response.text)

if __name__ == '__main__':
    run()

