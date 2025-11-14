pip install grpcio

pip3 install grpcio grpcio-tools

python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. mplane/notification_service.proto