#!/usr/bin/env python
# -*- coding=utf-8 -*-


"""
file: client.py
socket client
"""

import socket
import sys
import os
import struct




class MySocket:
    def __init__(self,sock=None):
        if sock is None:
            try:
                self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
                self.sock.connect(('192.168.1.190', 6666));
            except socket.error as msg:
                print (msg);
                sys.exit(1);
        else:
            self.sock = sock;
    def send_file(self):
        filepath = sounddata;
        if os.path.isfile(filepath):
            fileinfo_size=struct.calcsize('128sl');
            fhead = struct.pack('128sl',bytes(os.path.basename(filepath).encode('utf-8')),os.stat(filepath).st_size);
            self.sock.send(fhead);
            print("client, filepath: {}".format([filepath]));
            fo = open(filepath,'rb');
            while True:
                filedata=fo.read(1024);
                if not filedata:
                    break;
                self.sock.send(filedata);
            fo.close();
            self.sock.close();

def recordwav():
    os.system("arecord -Dhw:0,0 -f S16_LE -r 16000 -c 6 -d 1 sounddata.wav");
'''
def socket_client():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('127.0.0.1', 6666))
    except socket.error as msg:
        print (msg);
        sys.exit(1)
    print (s.recv(1024).decode());
    while 1:
        data = input('please input work: ')
        s.send(data.encode());
        print (s.recv(1024).decode());
        if data == 'exit':
            break
    s.close()
'''
def main():
    skt_send = MySocket();
    while True:
        recordwav();
        skt_send.send_file();

if __name__ == '__main__':
    main();
