import wave
import os
import numpy as np
#from scipy.fftpack import fft,ifft
import math
import cmath
#import matplotlib as plt

def record():
    os.system("arecord -Dhw:0,0 -f S16_LE -r 16000 -c 6 -d 1 sounddata.wav");
def readwav():
    f=wave.open("sounddata.wav",'rb');
    params=f.getparams();
    original_data_string=f.readframes(params[3]);
    original_data=np.fromstring(original_data_string,dtype=np.short);
    original_data.shape=-1,params[0];
    original_data=original_data.T;
    #print(original_data.shape);
    #print(params[2]);
    return original_data,params[2];
def das(data,fs,MicPos):
    MicNum = data.shape[0];
    NWIN=1024;
    hopsize=NWIN/2;
    NFFT=1024;
    df=fs/NFFT;
    fft_x=np.zeros((data.shape[0],NFFT),dtype=np.complex_);
    for i in range(MicNum):
        fft_x[i,:]=np.fft.fft(data[i,:],1024);
    #print(fft_x);
    #print(fft_x.shape);
    angel_curve=np.zeros(360);
    c=343;

    for deg in range(0,359):
        for ff in range(0,int((NFFT/2)-1)):
            k=2*math.pi*ff*df/c;
            kappa=np.array([math.cos(deg/180*math.pi),math.sin(deg/180*math.pi),0]);
            a=np.zeros((MicNum),dtype=np.complex_);
            for MicNo in range(0,MicNum-1):
                a[MicNo]=cmath.exp(complex(0,1)*k*np.dot(kappa,MicPos[:,MicNo]));
            w=np.conj(a);
            angel_curve[deg]=angel_curve[deg]+abs(np.dot(w,fft_x[:,ff]));
    #print(angel_curve)
    #print(np.argmax(angel_curve));
    return(np.argmax(angel_curve));
def main():
    #record();
    MicPos=(1/100)*np.array([[4.5*math.cos(120/180*math.pi),4.5*math.cos(60/180*math.pi),4.5,4.5*math.cos(-60/180*math.pi),4.5*math.cos(-120/180*math.pi),-4.5],[4.5*math.sin(120/180*math.pi),4.5*math.sin(60/180*math.pi),0,4.5*math.sin(-60/180*math.pi),4.5*math.sin(-120/180*math.pi),0],[0,0,0,0,0,0]]);
    #print(MicPos);
    #print(MicPos.shape);
    data,fs=readwav();
    max = das(data,fs,MicPos);
    print(max);
if __name__ == '__main__':
    main();
