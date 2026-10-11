# import required libraries
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv

# Sample frequency
freq = 44100

# Recording duration 
duration = 5



# start recorder with the given values of 
# duration and sample frequency

recording = sd.rec(int(duration*freq), samplerate=freq , channels=1)

# record audio for the given number of seconds
sd.wait()




# this will convert the Numpy array to an audio 
# file with the given sampling frequency
write("recording0.wav",freq,recording)



