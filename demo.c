#include "AudioFile.h"
#include <stdlib.h>
#include <unistd.h>
AudioFile<double> audioFile;

int main(int argc, char const *argv[]) {
    //system("arecord -Dhw:0,0 -f S16_LE -r 16000 -c 2 -d 1 hello.wav");
    audioFile.load ("./hello.wav");
    int sampleRate = audioFile.getSampleRate();
    int bitDepth = audioFile.getBitDepth();

    int numSamples = audioFile.getNumSamplesPerChannel();
    double lengthInSeconds = audioFile.getLengthInSeconds();

    int numChannels = audioFile.getNumChannels();
    bool isMono = audioFile.isMono();
    bool isStereo = audioFile.isStereo();
    audioFile.setNumChannels(6);
    audioFile.setNumSamplesPerChannel(20000);//chunck 0.5s
    // or, just use this quick shortcut to print a summary to the console
    audioFile.printSummary();

    AudioFile<double>::AudioBuffer buffer;

    return 0;
}
