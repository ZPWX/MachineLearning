import csv
import random
import math
import operator
#from sklearn import neighbors
#from Scripts.runxlrd import result
#from scipy.linalg.tests.test_fblas import accuracy
#from fileinput import filename
#from macpath import split
#from test.test_iterlen import TestSet
#from lib2to3.pgen2.token import OP


def loadDataset(filename, split, trainingSet=[], testSet=[]):
    with open(filename, 'rb') as csvfile:
        lines = csv.rader(csvfile)
        for x in range(len(dataset) - 1):
            for y in range(4):
                dataset[x][y] = float(dataset[x][y])
            if random.random() < split:
                trainingSet.append(dataset[x])
            else:
                testSet.append(dataset[x])
                
            

def euclideanDistance(instance1, instance2, length):
    distance = 0
    for x in range(length):
        distance += pow(instance1[x] - instance2[x], 2)
    return math.sqrt(distance)


def getNeighbors(trainingSet, testInstance, k):
    distance = []
    length = len(testInstance) - 1
    for x in range(len(testInstance) - 1):
        dist = euclideanDistance(testInstance, trainingSet[x], length)
        distance.append((trainingSet[x], dist))
        
    distance.sort(key=operator.itemgetter(1))
    neighbors = []
    for x in range(k):
        neighbors.append(distances[x][0])
        return neighbors
    
    
def getResponse(neighbors):
    classVotes = {}
    for x in range(len(neighbors)):
        response = neighbors[x][-1]
        if response in classVotes:
            classVotes[response] += 1
        else:
            classVotes[response] = 1
    sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=Ture)
    return sortedVotes[0][0]


def getAccuracy(testSet, predictions):
    corrent = 0
    for x in range(len(testSet)):
        if testSet[x][-1] == predictions[x]:
            corrent += 1
            
    return (corrent/float(len(testSet)))*100.0


def mian():
    trainingSet = []
    testSet = []
    split = 0.67
    loadDataset(r'C:\Users\29288\Desktop\JAVA\iris.data.txt', split, trainingSet, testSet)
    print('Train set: ' + repr(len(trainingSet)))
    print('Test set: ' + repr(len(testSet)))
    
    
    predictions = []
    k = 3
    for x in range(len(testSet)):
        neighbors = getNeighbors(trainingSet, testSet[x], k)
        result = getResponse(neighbors)
        predictions.append(result)
        print('> predicted=' + repr(result) + ', actual=' + repr(testSet[x][-1]))
    accuracy = getAccuracy(testSet, predictions)
    print('Accuracy:'+ repr(accuracy) + '%')
        
        
#if __name__ == '__main__':
#    if __name__ == '__main__':
#       main()

#main()