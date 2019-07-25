
#conding=gbk
from sklearn.feature_extraction import DictVectorizer

from sklearn import preprocessing
#import sklearn
from sklearn import tree
from sklearn.externals.six import StringIO
from xml.sax.handler import feature_external_ges
from numpy.core._internal import dummy_ctype
import csv
import graphviz
from sklearn.svm.libsvm import predict
#import numpy

# rt/rb: set in windows on 'rt';set in linux on 'rb';
allElectronicsData = open(r'C:\Users\29288\Desktop\JAVA\AllElectronics.csv','rt')
reader = csv.reader(allElectronicsData)
headers = next(reader)
print(headers)


featureList = []
labelList = []

for row in reader:
    labelList.append(row[len(row) - 1])
    rowDict = {}
    
    for i in range(1, len(row) - 1):
        rowDict[headers[i]] = row[i]
        
    featureList.append(rowDict)
    
print(featureList)

#  Vetorize feature
vec = DictVectorizer()
dummyX = vec.fit_transform(featureList).toarray()

print("dummyX:\n " + str(dummyX))
print(vec.get_feature_names())

print("labelList:" + str(labelList))

#  Vectorize class lables

lb = preprocessing.LabelBinarizer()
dummyY = lb.fit_transform(labelList)
print("dummyY:\n" + str(dummyY))

# Using decision tree for classification

clf = tree.DecisionTreeClassifier(criterion='entropy')
clf = clf.fit(dummyX, dummyY)
print("clf:" + str(clf))

# Visualize model
with open('allElectronicInfoGainOri.dot', 'w') as f:
    f = tree.export_graphviz(clf, feature_names=vec.get_feature_names(), out_file = f)
oneRowX = dummyX[0, :]
print("oneRowX: " + str(oneRowX))


# predicted 
#newRowX = oneRowX

#newRowX[0] = 1
#newRowX[2] = 0
#print("newRowX: " + str(newRowX))

#predictY = clf.predict(newRowX)
#print("predictedY: " + str(predictedY))


print('04-MachineLearning-01-DecisionTree ending')