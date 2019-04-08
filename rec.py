def rec_fun(lignenumber,duration):
	   import sounddevice as sd
	   import numpy as np
	   #duration = 15
	   fs = 44100
	   myrecording_data = sd.rec(int(duration * fs), samplerate=fs, channels=2, blocking = True)
	   from scipy.io import wavfile

		# Convert `data` to 32 bit integers:
	   myrecording = (np.iinfo(np.int32).max * (myrecording_data/np.abs(myrecording_data).max())).astype(np.int32)
	   import scipy.io.wavfile as wr
	   wr.write('C:/Users/Arbing/Desktop/Code/reponses/reponse'+str(lignenumber)+'.wav', 44100, myrecording)