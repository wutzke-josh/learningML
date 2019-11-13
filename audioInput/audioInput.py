import alsaaudio, time

import matplotlib.pyplot as plt

print("listening...")
time.sleep(.2)

audio = alsaaudio.PCM(alsaaudio.PCM_CAPTURE)
audio.setformat(alsaaudio.PCM_FORMAT_U16_LE)
audio.setrate(8000)
audio.setperiodsize(800)

sounds = []

for i in range(40):
    l, raw = audio.read()
    data = [0 for i in range(l)]
    for i in range(l):
        data[i] = (raw[i*2] + (raw[(i * 2) + 1] << 8))
    sounds.extend(data)


# data = [0 for i in range(l)]
# for i in range(100):
#     for i in range(80):
#         sounds.pop(0)
#     l, raw = audio.read()
#     for i in range(l):
#         data[i] = (raw[i*2] + (raw[(i * 2) + 1] << 8))
#     sounds.extend(data)
plt.plot(sounds)
plt.show()
