import tensorflow as tf

import os, alsaaudio, numpy

import matplotlib.pyplot as plt

from tensorflow import keras

with open("helloSamples", "rb") as helloFile:
    raw = list(helloFile.read())

# This code assumes n samples at 8000 Bytes/s with one second samples
# in PCM_FORMAT_U16_LE from pyalsaaudio module

trainHello = []
middleman = [0 for i in range(16000)]
print("sectioning hellos")
for i in range(len(raw) // 16000):
    print(i)
    for j in range(16000):
        middleman[-(j+1)] = raw.pop()
    trainHello.append(middleman)

os.system("clear")

print("processing hellos")
sound = [0 for i in range(8000)]
for i in range(len(trainHello)):
    print(i)
    raw = trainHello[i]
    for j in range(8000):
        sound[j] = (raw[j * 2] + (raw[(j * 2) + 1] << 8))
    trainHello[i] = sound

os.system("clear")

helloLabels = [0 for i in range(len(trainHello))]

with open("notHellos", "rb") as notHelloFile:
    raw = list(notHelloFile.read())

# This code assumes n samples at 8000 Bytes/s with one second samples
# in PCM_FORMAT_U16_LE from pyalsaaudio module

print("Sectioning not hellos")
trainNotHello = []
middleman = [0 for i in range(16000)]
for i in range(len(raw) // 16000):
    print(i)
    for j in range(16000):
        middleman[-(j+1)] = raw.pop()
    trainNotHello.append(middleman)

os.system("clear")
print("Processing not hellos")

sound = [0 for i in range(8000)]
for i in range(len(trainNotHello)):
    print(i)
    raw = trainNotHello[i]
    for j in range(8000):
        sound[j] = (raw[j * 2] + (raw[(j * 2) + 1] << 8))
    trainNotHello[i] = sound

os.system("clear")

notHelloLabels = [1 for i in range(len(trainNotHello))]

trainData = trainHello + trainNotHello
del trainHello
del trainNotHello

trainLabels = helloLabels + notHelloLabels
del helloLabels
del notHelloLabels

del raw

print("Data loaded")

trainData = [[(trainData[i][j] / (0xFFFF)) for j in range(len(trainData[i]))] for i in range(len(trainData))]

model = keras.Sequential([
    keras.layers.Dense(8000, activation='relu'),
    keras.layers.Dense(800, activation='relu'),
    keras.layers.Dense(2, activation='softmax')
])

model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

model.fit(trainData, trainLabels, epochs = 2)

audio = alsaaudio.PCM(alsaaudio.PCM_CAPTURE)
audio.setformat(alsaaudio.PCM_FORMAT_U16_LE)
audio.setrate(8000)
audio.setperiodsize(80)

sound = [0 for i in range(8000)]

for i in range(100):
    audio.read()

for i in range(200):
    for i in range(7920):
        sound[i] = sound[i+80]
    l, newSample = audio.read()
    for i in range(80):
        sound[i+7920] = (newSample[i * 2] + (newSample[((i * 2) + 1)] << 8))

    # guess = model.predict([sound])
    # guess = numpy.argmax(guess[0])

    # if not guess:
    #     print("Hello")

plt.plot(sound)
plt.show()
