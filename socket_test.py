import socket
import time

max_bit = 65555

if __name__ == '__main__':
    # hostname = 'www.fuckalipapa.tk'
    # ip_addres = socket.gethostbyname(hostname)
    # print(ip_addres)
    c_sock = socket.socket(type=socket.SOCK_STREAM)
    c_sock.bind(('172.21.15.216', 0))
    text = 'bhfdjka'
    data = text.encode('utf-8')
    c_sock.connect(('172.21.13.121', 8868))
    print(c_sock.getsockname())
    
    time.sleep(10)
    c_sock.close()
    # c_sock.sendto(data, ('172.21.13.121', 1080))
    # data, addres = c_sock.recvfrom(6555)
    # text = data.decode('utf-8')
    # print(addres,text)
