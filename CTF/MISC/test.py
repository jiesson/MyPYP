import numpy as np
from PIL import Image
import math
import operator
import os
import time
import base64
import random

def load_horse():
    data = []
    p = Image.open('./horse.png').convert('L')
    p = np.array(p).reshape(-1)
    p = np.append(p,0)
    data.append(p)
    return np.array(data)

def load_deer():
    data = []
    p = Image.open('./deer.png').convert('L')
    p = np.array(p).reshape(-1)
    p = np.append(p,1)
    data.append(p)
    return np.array(data)

def load_test(pic):
    data = []
    p = Image.open(pic).convert('L')
    p = np.array(p).reshape(-1)
    p = np.append(p,1)
    data.append(p)
    return np.array(data)


def euclideanDistance(instance1, instance2, length):
    distance = 0
    for x in range(length):
        distance += pow((instance1[x] - instance2[x]), 2)
    return math.sqrt(distance)


def getNeighbors(trainingSet, testInstance, k):
    distances = []
    length = len(testInstance) - 1
    for x in range(len(trainingSet)):
        dist = euclideanDistance(testInstance, trainingSet[x], length)
        distances.append((trainingSet[x], dist))
    distances.sort(key=operator.itemgetter(1))
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
    sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
    return sortedVotes[0][0]


def getAccuracy(testSet, predictions):
    correct = 0
    for x in range(len(testSet)):
        if testSet[x][-1] == predictions[x]:
            correct += 1
    return (correct / float(len(testSet))) * 100.0

def check(pic):
    source_p = Image.open('deer.png')
    try:
        c_p = Image.open(pic)
    except:
        print("Please upload right picture.")
        exit()
    diff_pixel = 0
    a, b = source_p.size
    if c_p.size[0] != a and c_p.size[1] != b:
    	print("Please upload right picture size("+str(a)+','+str(b)+')')
    	exit()
    for y in range(b):
        for x in range(a):
            diff_pixel += abs(source_p.getpixel((x, y)) - c_p.getpixel((x, y)))
    return diff_pixel

ss=load_test('m.jpg')
print((ss))