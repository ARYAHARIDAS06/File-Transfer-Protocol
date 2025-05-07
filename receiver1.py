import socket
import os

# Configuration
HOST = 'localhost'
PORT = 5001
SHARED_PASSWORD = "secret123"
DEST_FOLDER = 'folder2'
DEST_FILENAME = 'received_example1.txt'

# Ensure destination folder exists
os.makedirs(DEST_FOLDER, exist_ok=True)
dest_path = os.path.join(DEST_FOLDER, DEST_FILENAME)

# Start the server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)
print(f"Receiver: Listening on {HOST}:{PORT}...")

client_socket, addr = server_socket.accept()
print(f"Receiver: Connection from {addr}")

# Step 1: Authenticate
received_password = client_socket.recv(1024).decode()
if received_password != SHARED_PASSWORD:
    print("Receiver: Authentication failed.")
    client_socket.send("AUTH_FAIL".encode())
    client_socket.close()
    server_socket.close()
    exit()

client_socket.send("AUTH_OK".encode())
print("Receiver: Authentication successful.")

# Step 2: Receive file data
with open(dest_path, 'wb') as f:
    print("Receiver: Starting to receive file data...")
    while True:
        data = client_socket.recv(1024)
        if not data:
            print("Receiver: No more data received.")
            break
        print(f"Receiver: Received {len(data)} bytes.")
        f.write(data)
    f.flush()

print(f"Receiver: File saved to {dest_path}")

# Step 3: Acknowledge
client_socket.send("RECEIVED".encode())

# Cleanup
client_socket.close()
server_socket.close()
