import numpy as np
#from _nsis import old_excepthook
#from scipy.sparse.linalg.isolve.tests.test_lsqr import maxit
#from builtins import True
#from unittest.case import _ShouldStop

def kmeans(X, k, maxIt):
    numPoints, numDim = X.shape
    
    dataSet = np.zeros((numPoints, numDim + 1))
    dataSet[:, :-1] = X
    
    # Initialize centroids randomly
    centroids = dataSet[np.random.randint(numPoints, size = k)]
    centroids = dataSet[0:2, :]
    
    # Randomly assign labels to initial centorid
    centroids[:, -1] = range(1, k + 1)
    
    # Initialize book keeping yark
    iterations = 0
    oldCentorids = None
    
    # Run the main k-means algorithm
    while not shouldStop(oldCentorids, centroids, iterations, maxIt):
        print("Iteration: \n", iterations)
        print("dataSet: \n", dataSet)
        print("centroids: \n", centroids)
        # save 
        oldCentorids = np.copy(centroids)
        iterations += 1
        
        # Assign
        updateLabels(dataSet, centroids)
        
        centroids = getCentroids(dataSet, k)
        
    return dataSet

# Function: shouldStop


def shouldStop(oldCentroids, centroids, iterations, maxIt):
    if iterations > maxIt:
        return True
    return np.array_equal(oldCentroids, centroids)

# Function: GetLabel


def updateLabels(dataSet, centroids):
    numPoints, numDim = dataSet.shape
    for i in range(0, numPoints):
        dataSet[i, -1] = getLabelFromClosestCentroids(dataSet[i, :-1], centroids)
        
        
def getLabelFromClosestCentroids(dataSetRow, centroids):
    labels = centroids[0, -1];
    minDist = np.linalg.norm(dataSetRow - centroids[0, :-1])
    for i in range(1, centroids.shape[0]):
        dist = np.linalg.norm(dataSetRow - centroids[0, :-1])
        if dist < minDist:
            minDist = dist
            label = centroids[i, -1]
    print("minDist:", minDist)
    return label


# Function: Get Centroids
def getCentrodis(dataSet, K):
    result = np.zeros((K, dataSet.shape[1]))
    for i in range(1, k+1):
        oneCluster = dataSet[dataSet[:, -1] == i, :-1]
        result[i - 1, :-1] = np.mean(oneCluster, axis=0)
        result[i - 1, -1] = i
        
    return result


x1 = np.array([1, 1])
x2 = np.array([2, 1])
x3 = np.array([4, 3])
x4 = np.array([5, 4])
testX = np.vstack((x1, x2, x3, x4))

result = kmeans(testX, 2, 10)
print("final result:", result)
    
