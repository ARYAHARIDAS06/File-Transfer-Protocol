# File-Transfer-Protocol
Simple File Transfer Protocol Using Python
This project demonstrates a simple, secure file transfer system using Python's built-in socket library. It allows a sender to transfer a file over a TCP connection to a receiver after verifying a shared password for authentication.

The system is ideal for learning about:

Socket programming in Python

Basic network communication (client-server model)

Secure transmission using password-based access control

It includes two main scripts:

sender.py: Initiates a connection, authenticates with the receiver, and transmits the file in chunks.

receiver.py: Listens for incoming connections, authenticates the sender, and saves the received file.

The transferred file is stored in a predefined folder on the receiver’s side, and the sender receives a confirmation after successful transfer.
