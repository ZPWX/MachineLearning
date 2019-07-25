import numpy as np
import pylab as pl
from sklearn import svm

np.random.seed(0)
X = np.r_[np.random.rand(20, 2) - [2, 2], np.random.randn(20, 2) + [2, 2]]
Y = [0] * 20 + [1] * 20

# fit the model
clf = svm.SVC(kernel='linear')
clf.fit(X, Y)


# get the separating hyperolne
w = clf.coef_[0]
a = -w[0]/w[1]
xx = np.linspace(-5, 5)
yy = a * xx - (clf._intercept_[0]/w[1])

# plot the
b = clf.support_vectors_[0]
yy_down = a * xx + (b[1] - a * b[0])
b = clf.support_vectors_[-1]
yy_up = a * xx + (b[1] - a * b[0])

print ("w:",  w)
print ("a:",  a)


print("support_vectors_:", clf.support_vectors_)
print("clf.coef_:", clf.coef_)

pl.plot(xx, yy, 'k-')
pl.plot(xx, yy_down, 'k--' )
pl.plot(xx, yy_up, 'k--')

pl.scatter(clf.support_vectors_[:, 0], clf.support_vectors_[:, 1], s = 80, facecolors='none')

pl.axis('tight')
pl.show()