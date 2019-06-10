import wave
import sys
import numpy as np

def readwav():
    f=wave.open("hello.wav",'rb');
    params=f.getparams();
    original_data_string=f.readframes(params[3]);
    original_data=np.fromstring(original_data_string,dtype=np.short);
    original_data.shape=-1,params[0];
    original_data=original_data.T;
    print(original_data.shape);
def main():
    readwav();
if __name__ == '__main__':
    main();
