#include "AudioFile.h"
#include <stdlib.h>
#include <unistd.h>
AudioFile<double> audioFile;

int main(int argc, char const *argv[]) {
    //system("arecord -Dhw:0,0 -f S16_LE -r 16000 -c 2 -d 1 hello.wav");
    audioFile.load ("./hello.wav");
    return 0;
}
