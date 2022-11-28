import numpy
import soundfile
import librosa

samplerate = 22050
song,sr = librosa.load("shotgun.mp3", sr=samplerate)

outsong = numpy.empty( int(song.size*2) )

outsong[::2]  = song
outsong[1::2] = song

soundfile.write("try2.wav", outsong, samplerate, subtype='PCM_24')
