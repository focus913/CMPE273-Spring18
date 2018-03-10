import zmq
import sys
from _thread import start_new_thread

# ZeroMQ Context
context = zmq.Context()
name = sys.argv[1]

def receiver():
    sock = context.socket(zmq.SUB)
    sock.setsockopt_string(zmq.SUBSCRIBE, '')
    sock.connect("tcp://127.0.0.1:5679")
    while True:
        username, msg = sock.recv_pyobj()
        if name != username:
            print('\r[%s]: %s\n[%s]>' % (username, msg, name), end='')

def run():
    sock = context.socket(zmq.REQ)
    sock.connect("tcp://127.0.0.1:5678")
    print('User ' + sys.argv[1] + ' Connected to the chat server.')

    start_new_thread(receiver, ())
    while True:
        msg = input('[%s]>' % name)
        sock.send_pyobj((name, msg))
        sock.recv_string()

if __name__ == '__main__':
    run()

'''
(my-venv) YuematoMacBook-Pro:lab3 yinyue913$ python client.py Alice
User Alice Connected to the chat server.
[Bob]: Hello From Bob!
[Bob]: Hello World from Bob!
[Alice]>Hello From Alice!
[Alice]>Hello World from Alice!
[Alice]>


(my-venv) YuematoMacBook-Pro:lab3 yinyue913$ python client.py Alice
User Alice Connected to the chat server.
[Bob]: Hello From Bob!
[Bob]: Hello World from Bob!
[Alice]>Hello From Alice!
[Alice]>Hello World from Alice!
[Alice]>
