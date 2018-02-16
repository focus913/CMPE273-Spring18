from __future__ import print_function

import grpc

from pingpong_pb2 import Request, Response
import pingpong_pb2_grpc


class PingClient():
    def __init__(self, host='0.0.0.0', port=3000):
        self.channel = grpc.insecure_channel('%s:%d' % (host, port))
        self.stub = pingpong_pb2_grpc.PingPongStub(self.channel)

    def ping(self, data):
        req = Request(data=str(data))
        return self.stub.ping(req)


def test():
    client = PingClient()
    response = client.ping("ping")
    print("Response={}".format(response.data))


if __name__ == '__main__':
    test()
