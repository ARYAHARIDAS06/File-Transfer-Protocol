import socket
import os

# Configuration
HOST = 'localhost'
PORT = 5001
SHARED_PASSWORD = "secret123"
SOURCE_FOLDER = 'folder1'
FILENAME = 'example.txt'
file_path = os.path.join(SOURCE_FOLDER, FILENAME)

# Verify file exists
if not os.path.exists(file_path):
    print(f"Sender: File not found at {file_path}")
    exit()

# Connect to receiver
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))
print(f"Sender: Connected to {HOST}:{PORT}")

# Step 1: Send password
client_socket.send(SHARED_PASSWORD.encode())
auth_reply = client_socket.recv(1024).decode()

if auth_reply != "AUTH_OK":
    print("Sender: Authentication failed. Exiting.")
    client_socket.close()
    exit()

print("Sender: Authentication successful.")

# Step 2: Send file
with open(file_path, 'rb') as f:
    print("Sender: Starting to send file data...")
    while True:
        data = f.read(1024)
        if not data:
            break
        client_socket.sendall(data)
        print(f"Sender: Sent {len(data)} bytes.")

# Signal end of transmission
client_socket.shutdown(socket.SHUT_WR)

# Step 3: Wait for acknowledgment
ack = client_socket.recv(1024).decode()
if ack == "RECEIVED":
    print("Sender: Receiver confirmed successful transfer.")
else:
    print("Sender: No confirmation received.")

client_socket.close()
