#!/usr/bin/env python
# -*- coding=utf-8 -*-


"""
file: service.py
socket service
"""


import socket
import threading
import time
import sys
import time,struct,os


class MySocket:
    def __init__(self,sock=None):
        if sock is None:
            try:
                self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
                self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                self.sock.bind(('192.168.1.190', 6666))
                self.sock.listen(10)
            except socket.error as msg:
                print (msg);
                sys.exit(1);
        else:
            self.sock = sock;
    def start(self):
        print("wait for connect..........");
        conn, addr = self.sock.accept()
        t = threading.Thread(target=file, args=(conn, addr))
        t.start();

def file(conn,addr):
    fileinfo_size=struct.calcsize('128sl');
    buf = conn.recv(fileinfo_size);
    print(size(buf))
    filename,filesize = struct.unpack('128sl',buf);
    filename_f = filename.decode().strip('\00');
    filename_f = "new_"+filename_f;
    print("file name = {}".format(filename_f));
    recvd_size = 0;
    file = open(filename_f,'wb');
    conn.send("ready");
    print ('stat receiving...');
    while not recvd_size == filesize:
        if filesize - recvd_size > 1024:
            rdata = conn.recv(1024);
            recvd_size += len(rdata);
        else:
            rdata = conn.recv(filesize - recvd_size);
            recvd_size = filesize;
        file.write(rdata);
    file.close();
    print("receive done");

    conn.close();
'''
def deal_data(conn, addr):
    print ('Accept new connection from {0}'.format(addr));
    conn.send("Hi, Welcome to the server!".encode());
    while 1:
        data = conn.recv(1024).decode()
        print ('{0} client send data is {1}'.format(addr, data));
        #time.sleep(1)
        if data == 'exit' or not data:
            print ('{0} connection close'.format(addr));
            conn.send('Connection closed!'.encode());
            break
        conn.send('Hello, {0}'.format(data).encode());
    conn.close()
'''

def main():
    skt=MySocket();
    skt.start();
if __name__ == '__main__':
    main();
