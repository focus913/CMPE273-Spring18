# CMPE273-Spring18
# Compile the proto file
```sh
python -m grpc_tools.protoc -I./ --python_out=. --grpc_python_out=. pingpong.proto
```
