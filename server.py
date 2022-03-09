import socket
import _thread
from player import player
import pickle

server = "192.168.1.41"
port = 5555

sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

players = [player(0, 0, 50, 50, (255, 0, 0)), player(0, 0, 50, 50, (0, 0, 255))]

try:
    sckt.bind((server, port))
except socket.error as error:
    print(str(error))

sckt.listen(2)
print("Waiting for a connection, Server Started")

def threadedClient(conn, player):
    conn.send(pickle.dumps(players[player]))
    reply = ""
    while True:
        try:
            data = pickle.loads(conn.recv(2048))
            players[player] = data 
            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = players[0]
                else:
                    reply = players[1]
            conn.sendall(pickle.dumps(reply))
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