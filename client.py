import socket
import os
ip = '127.0.0.1'
port = 8080

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
os.system('clear')
print("Messaging is now LIVE\n____________________")

while True:
    send_data = input("\t\t\t\t\tClient (You): ");
    if send_data == "</>":
        print("--------------------\nPROGRAM MESSAGE: Terminated\n--------------------")
        s.sendto(send_data.encode(), (ip,port))
        s.close()
        exit()
    s.sendto(send_data.encode(), (ip, port))
    data, address = s.recvfrom(4096)
    if data.decode() == "</>":
        print("--------------------\nPROGRAM MESSAGE: Terminated\n--------------------")
        s.close()
        exit()
    print("Server (Person 2): ", data.decode())

s.close()