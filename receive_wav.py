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
import wave
import numpy as np
from respeaker import das,readwav
#from scipy.fftpack import fft,ifft
import math
import cmath

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
        t = threading.Thread(target=start, args=(conn, addr))
        t.start();
def start(conn,addr):
    while True:
        file(conn,addr);
        pos = location();
        print("location = {}".format(pos));
        reply_pos(conn,addr,pos);

def location():
    MicPos=(1/100)*np.array([[4.5*math.cos(120/180*math.pi),4.5*math.cos(60/180*math.pi),4.5,4.5*math.cos(-60/180*math.pi),4.5*math.cos(-120/180*math.pi),-4.5],[4.5*math.sin(120/180*math.pi),4.5*math.sin(60/180*math.pi),0,4.5*math.sin(-60/180*math.pi),4.5*math.sin(-120/180*math.pi),0],[0,0,0,0,0,0]]);
    data,fs=readwav();
    max = das(data,fs,MicPos);
    return max

def reply_pos(conn,addr,pos):
    conn.send("pos = {}".format(max));

def file(conn,addr):
    fileinfo_size=struct.calcsize('128sQ');
    buf = conn.recv(fileinfo_size);
    print(len(buf));
    print(buf);
    #l in respeaker is 4 byte but 4 byte in notebook
    filename,filesize = struct.unpack('128sQ',buf);
    filename_f = filename.decode().strip('\00');
    #filename_f = "new_"+filename_f;
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

    #conn.close();
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
