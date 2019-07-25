
from sklearn import neighbors
from sklearn import datasets
from sklearn.svm.libsvm import predict

knn = neighbors.KNeighborsClassifier()

iris = datasets.load_iris()

print(iris)

# KNN build mode

knn.fit(iris.data, iris.target)

# predicted 
predictedLabel = knn.predict([[0.1, 0.2, 0.3, 0.4]])

print('hello')

print(predictedLabel)