import zmq

# ZeroMQ Context
context = zmq.Context()

# Define the socket using the "Context"
sock = context.socket(zmq.REP)
sock.bind("tcp://127.0.0.1:5678")
sock1 = context.socket(zmq.PUB)
sock1.bind("tcp://127.0.0.1:5679")

# Run a simple "Echo" server
while True:
    username, message = sock.recv_pyobj()
    sock.send_string("")
    sock1.send_pyobj((username, message))
