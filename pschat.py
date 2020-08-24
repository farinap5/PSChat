import socket

def serveside():
    print("-----Chat Server-----")
    ip = "0.0.0.0"
    port = int(input("Set port: "))
    name = input("Your name: ")

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("[\033[1;33m!\033[0;0m]- Starting Server.")
    server.bind((ip, port))
    server.listen(5)
    print("[\033[1;32mOK\033[0;0m]- Listening -",port)
    print("\033[1;32m---------------------\033[0;0m")

    (client_sock, addr) = server.accept()
    print("[\033[1;32mOK\033[0;0m] - ",addr[0], "-", addr[1])

    while True:
        data = client_sock.recv(1024)
        print(data.decode())
        resp = input("Your Turn> ")
        res = name + " - " + resp
        client_sock.send(res.encode())

    server.close()
def clientside():
    print("-----Chat Client-----")
    ip = input("Set Host: ")
    port = int(input("Set port: "))
    name = input("Your name: ")

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("[\033[1;33m!\033[0;0m]- Starting Connection.")

    print("[\033[1;33m!\033[0;0m]- Searching For Host.")
    client.connect((ip,port))
    print("\033[1;32m---------------------\033[0;0m")
    print("[\033[1;32mOK\033[0;0m]- Say Something!")
    while True:
        resp = input("Yout Turn> ")
        res = name + " - " + resp
        client.send(res.encode())
        data = client.recv(1024)
        print(data.decode())


def main():
    print("Simple Socket Chat .v1\nby_farinap05\n")
    l = ["Services:","[1]-Client Side","[2]-Server Side","[0]-Exit\n"]
    for i in l:
        print(i)
    op = int(input(" >> "))
    if op == 1:
        clientside()
    if op == 2:
        serveside()
    if op == 0:
        exit("GOOD BEY!")
    else:
        print("Uknow Option!")
        main()

try:
    main()
except KeyboardInterrupt:
    print("\033[1;32mOK\033[0;0m")






