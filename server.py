import socket
import os
ip = '127.0.0.1'
port = 8080

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = (ip, port)
s.bind(server_address)
os.system('clear')
print("Messaging is now LIVE\n____________________")

while True:
    data, address = s.recvfrom(4096)
    if data.decode() == "</>":
        print("--------------------\nPROGRAM MESSAGE: Terminated\n--------------------")
        s.close()
        exit()
    print("Client (Person 2): ", data.decode())
    send_data = input("\t\t\t\t\tServer(You): ")
    if send_data == "</>":
        print("--------------------\nPROGRAM MESSAGE: Terminated\n--------------------")
        s.sendto(send_data.encode(), address)
        s.close()
        exit()
    s.sendto(send_data.encode(), address)