import numpy as np
import csv
import math
from copy import deepcopy
from collections import Counter

def loadCsv(filename):
    lines = csv.reader(open(filename, "rb"))
    next(lines,None)
    dataset = list(lines)
    for i in range(len(dataset)):
        dataset[i] = [x for x in dataset[i]]
    return dataset

def kmeans(dataset, k):
    centroids = []

    data = np.array(dataset)[:, [0, 1]]
    centroids = randomize(data, centroids, k)
    prev_centroids = [[] for i in range(k)]

    iterations = 0
    while not (reached_thres(centroids, prev_centroids, iterations)):
        iterations += 1
        clusters = [[] for i in range(k)] # assign data points to the clusters
        clusters = euclidean(data, centroids, clusters)
        x_sum = 0.0
        y_sum = 0.0
        x_list = []
        y_list = []
        cluster_len = []

        prev_centroids = deepcopy(centroids)
        for cluster in clusters:
            x_sum = 0.0
            y_sum = 0.0
            for points in cluster:
                x_sum += float(points[0])
                y_sum += float(points[1])
            x_list.append(x_sum)
            y_list.append(y_sum)
            cluster_len.append(len(cluster))

        for i in range(len(cluster_len)):
            x_mean = x_list[i] / cluster_len[i]
            y_mean = y_list[i] / cluster_len[i]
            centroids[i][0][0][0] = x_mean
            centroids[i][0][0][1] = y_mean

        print("The total number of data instances is: " + str(len(data)))    
        print("The mean value of each cluster: " + str(centroids))
        print("The clusters starts:")
    
        index = 0
        for cluster in clusters:
               crime =[]
               clusterList = np.array(cluster).tolist()
               for i in range(len(dataset)):
                   for j in range(len(clusterList)):
                        if dataset[i][0] == clusterList[j][0] and dataset[i][1] == clusterList[j][1]:
                            crime.append(dataset[i][2])
               clusterfile = open('cluster.csv', 'a')
               clusterfile.write("Cluster")
               clusterfile.write(",")
               clusterfile.write("%s" % index)
               clusterfile.write("\n")
               for i in range(len(clusterList)):
                   clusterfile.write("%s" % clusterList[i][1])
                   clusterfile.write(",")
                   clusterfile.write("%s" % clusterList[i][0])
                   clusterfile.write("\n")
               
               count = Counter(crime)
               countfile = open('count.csv', 'a')
               countfile.write("Cluster")
               countfile.write(",")
               countfile.write("%s" % index)
               countfile.write("\n")
               
               
               freq_list = count.values()
               max_cnt = max(freq_list) #max_cnt #max count of the most occuring crime
               total = freq_list.count(max_cnt)
               most_common = count.most_common(total)
               print "count ", count #count of all the crimes in that cluster
               print "most common", count.most_common()
               most = count.most_common()
               for elem in most:
                  countfile.write(elem[0])
                  countfile.write(",")
                  countfile.write("%s" % elem[1])
                  countfile.write("\n")
                  print elem[0]
               index +=1
               print("Cluster ends")
    return


def euclidean(data, centroids, clusters):
    for instance in data:
        x, y = instance
        distance = []
        for centroid in centroids:
            cx = centroid
            cx_new = cx[0][0][0]
            cy_new = cx[0][0][1]
            distance.append(math.sqrt(abs((float(x) - float(cx_new)) ** 2 + (float(y) - float(cy_new)) ** 2))) # Calculates euclidean distance between
        value = min(distance)
        mu_index = distance.index(value)

        try:
            clusters[mu_index].append(instance)
        except KeyError:
            clusters[mu_index] = [instance]

    for cluster in clusters:
        if not cluster:
            cluster.append(data[np.random.randint(0, len(data), size=1)])
            
    return clusters  

def randomize(data, centroids, k):
    for cluster in range(0, k):
        centroids.append([data[np.random.randint(0, len(data), size=1)]])# randomize initial centroids
    return centroids
    
def reached_thres(centroids, old_centroids, iterations): #threshold condition
    MAX_ITERATIONS = 10
    if iterations > MAX_ITERATIONS:
        return True
    if iterations > 0:
        for i in range(len(centroids)):
            if old_centroids[i][0][0][0] != centroids[i][0][0][0]:
                return False
        return True
    else:
        return False

def main():
    filename = 'diabetes.csv'
    dataset = loadCsv(filename)
    k = 2
    kmeans(dataset, k)

main()

