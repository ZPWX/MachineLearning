from sklearn.datasets import load_digits
#from handWritedNumberNN import digits

digits = load_digits()
print(digits.data.shape)

import pylab as pl
pl.gray()
pl.matshow(digits.images[1])
pl.show()
