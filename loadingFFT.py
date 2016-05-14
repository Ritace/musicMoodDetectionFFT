import glob
import scipy
import os
import numpy as np
from scipy.io import wavfile



def read_fft(genre_list, base_dir):
	X = []
	y = []
	for label, genre in enumerate(genre_list):
		
		genre_dir = os.path.join(base_dir, genre, "*.fft.npy")
		# print genre_dir
		file_list =glob.glob(genre_dir)
		for fn in file_list:
			fft_features = scipy.load(fn)
			X.append(fft_features[:1000])
			y.append(label)
	return np.array(X), np.array(y)
# X= []
# y = []
genre_list = ["blues","classical","country","disco","hiphop","jazz","metal","pop","reggae","rock"]
genre_dir = "/home/ritesh/R/musicmoodanalysis/musicMood_FFT/genres/"
X,Y = read_fft(genre_list,genre_dir)
# print X
# print Y

from sklearn.naive_bayes import GaussianNB

clf = GaussianNB()
clf.fit(X, Y)

def predict(file_path):
	#predicting here given the file path
	sample_rate, X = scipy.io.wavfile.read(file_path)
	fft_features = abs(scipy.fft(X)[:1000])
	# print(fft_features[:1000])
	print(clf.predict(fft_features[:1000]))
predict("/home/ritesh/R/musicmoodanalysis/musicMood_FFT/genres/test/test.classical.00006.wav")
predict("/home/ritesh/R/musicmoodanalysis/musicMood_FFT/genres/test/test.rock.00006.wav")
predict("/home/ritesh/R/musicmoodanalysis/musicMood_FFT/genres/test/test.classical.00009.wav")
predict("/home/ritesh/R/musicmoodanalysis/musicMood_FFT/genres/test/test.classical.00001.wav")
predict("/home/ritesh/R/musicmoodanalysis/musicMood_FFT/genres/test/test.metal.00006.wav")
predict("/home/ritesh/R/musicmoodanalysis/musicMood_FFT/genres/test/test.rock.00000.wav")


