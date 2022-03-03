import socket
import _thread
import sys

server = "192.168.1.41"
port = 5555

sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def readPos(str):
    str = str.split(",")
    return int(str[0]), int(str[1])

def makePos(tup):
    return str(tup[0]) + "," + str(tup[1])
 
pos = [(0,0), (100,100)]

try:
    sckt.bind((server, port))
except socket.error as error:
    print(str(error))

sckt.listen(2)
print("Waiting for a connection, Server Started")

def threadedClient(conn, player):
    conn.send(str.encode(makePos(pos[player])))
    reply = ""
    while True:
        try:
            data = readPos(conn.recv(2048).decode())
            pos[player] = data
            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = pos[0]
                else:
                    reply = pos[1]
            conn.sendall(str.encode(makePos(reply)))
        except:
            break
    print("Lost connection")
    conn.close()

currentPlayer = 0
while True:
    conn, addr = sckt.accept()
    print("Connected to:", addr)

    _thread.start_new_thread(threadedClient, (conn, currentPlayer))
    currentPlayer += 1