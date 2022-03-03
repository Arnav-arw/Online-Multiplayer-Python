import socket
import _thread
import sys

server = "192.168.1.41"
port = 5555

sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    sckt.bind((server, port))
except socket.error as error:
    print(str(error))

sckt.listen(2)
print("Waiting for a connection, Server Started")

def threadedClient(conn):
    conn.send(str.encode("Welcome, type your info\n"))
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode("utf-8")
            if not data:
                print("Disconnected")
                break
            else:
                print("Received: ", reply)
            conn.sendall(str.encode(reply))
        except:
            break

while True:
    conn, addr = sckt.accept()
    print("Connected to:", addr)

    _thread.start_new_thread(threadedClient, (conn,))