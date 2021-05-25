import socket
import threading

nick = input("Wprowadz Nickname: ")
adress = input("Wprowadz Adress: ")
if(adress == "globalchat"):
    adress = "34.89.133.142"
    port = 6677
else:
    port = int(input("Wprowadz Port: "))

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((adress, port))

def start():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == "NICK":
                client.send(nick.encode('ascii'))
            else:
                print(message)
        except:
            print("Wystapil Nieoczekiwany Blad!")
            client.close()
            break

def pisanie():
    while True:
        m = input()
        message = f'{nick}: {m}'
        client.send(message.encode('ascii'))

wysylanie = threading.Thread(target=start)
wysylanie.start()

pisanie = threading.Thread(target=pisanie)
pisanie.start()