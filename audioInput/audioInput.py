import alsaaudio, time

import matplotlib.pyplot as plt

import os

audio = alsaaudio.PCM(alsaaudio.PCM_CAPTURE)
audio.setformat(alsaaudio.PCM_FORMAT_U16_LE)
audio.setrate(8000)
audio.setperiodsize(80)
# audio.pause(1)
os.system("clear")

# I'm not sure what an appropriate extenstion is...
with open("helloSamples", "wb") as sounds:
    for i in range(20):
        print("again")
        time.sleep(.2)
        os.system("clear")
        for j in range(100):
            # audio.pause(0)
            l, raw = audio.read()
            # audio.pause(1)
            sounds.write(raw)



### This code will probably be useful to unpack the bytestream when opening the files for training
# for i in range(l):
#     data[i] = (raw[i*2] + (raw[(i * 2) + 1] << 8))
# sounds.extend(data)
