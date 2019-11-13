import alsaaudio, time

audio = alsaaudio.PCM(alsaaudio.PCM_PLAYBACK)
audio.setformat(alsaaudio.PCM_FORMAT_U16_LE)
audio.setrate(8000)
audio.setperiodsize(80)


with open("helloSamples", "rb") as soundFile:
    raw = list(soundFile.read())

data = []
for i in range(len(raw) // 80):
    middleman = []
    for j in range(80):
        middleman.append(raw.pop(0))
    middleman = bytes(middleman)
    data.append(middleman)

for noise in data:
    audio.write(noise)


# for i in range():
#     data[i] = (raw[i*2] + (raw[(i * 2) + 1] << 8))
# sounds.extend(data)