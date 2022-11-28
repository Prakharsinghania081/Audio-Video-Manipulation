import numpy
import soundfile
import librosa

samplerate = 22050
song,sr = librosa.load("iml.mp3", sr=samplerate)

outsong = song[::2] + song[1::2]
outsong = outsong/2

soundfile.write("try.wav", outsong, samplerate, subtype='PCM_24')
