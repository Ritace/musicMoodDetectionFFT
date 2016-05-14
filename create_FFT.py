#here going to implement the algorithm

import os
import scipy 
from scipy.io import wavfile

def create_fft(fn):
	sample_rate, X = scipy.io.wavfile.read(fn)
	fft_features = abs(scipy.fft(X)[:1000])
	
	base_fn, ext = os.path.splitext(fn)
	data_fn = base_fn + ".fft"
	scipy.save(data_fn, fft_features)
#directory the fft lies in
base_dir = "/home/ritesh/R/musicmoodanalysis/musicMood_FFT/genres/"
# location = "/home/ritesh/R/musicmoodanalysis/musicMood_FFT/genres/blues/output.wav"
genre_list = ["classical","country","disco","hiphop","jazz","metal","pop","reggae","rock"]
for genre in genre_list:
	directory = base_dir + genre + "/"+genre+"." +"000" 
	for i in range(0,100):

		if i < 10:
			fft_dir = directory +"0"+ str(i)+".wav"
		else:
			fft_dir = directory + str(i)+".wav"
		print fft_dir
		create_fft(fft_dir)
		
	print directory

# create_fft(location)
