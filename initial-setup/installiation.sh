# Install pipx if not already installed
sudo apt install pipx

# Ensure pipx is properly set up
pipx ensurepath

# Install InquirerPy in an isolated environment
pipx install InquirerPy



# This will store the requirements in the file
pipdeptree --freeze > requirements.txt

# Install pipdeptree
sudo apt install python3-pipdeptree



pip install grpcio

pip3 install grpcio grpcio-tools

python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. mplane/notification_service.proto
