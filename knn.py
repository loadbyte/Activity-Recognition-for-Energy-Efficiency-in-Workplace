# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 11:14:06 2017
@author: Subash, Anirban
"""
# import modules
import csv
import random
import math
import operator

# method definations
def uploadDataset(fname, split, trainingData=[] , testData=[]):
	with open(fname, 'r') as csvFileFormat:
	    lines = csv.reader(csvFileFormat)
	    dataset = list(lines)
	    for x in range(len(dataset)-1):
	        for y in range(3):
	            dataset[x][y] = float(dataset[x][y])
	        if random.random() < split:
	            trainingData.append(dataset[x])
	        else:
	            testData.append(dataset[x])

def euclideanDist(inst1, inst2, leng):
	dist = 0
	for x in range(leng):
		dist += pow((inst1[x] - inst2[x]), 2)
	return math.sqrt(dist)

def getNeighbors(trainingData, testInst, k):
	distances = []
	leng = len(testInst)-1
	for x in range(len(trainingData)):
		dist = euclideanDist(testInst, trainingData[x], leng)
		distances.append((trainingData[x], dist))
	distances.sort(key=operator.itemgetter(1))
	neighbors = []
	for x in range(k):
		neighbors.append(distances[x][0])
	return neighbors

def getResponse(neighbors):
	votes = {}
	for x in range(len(neighbors)):
		res = neighbors[x][-1]
		if res in votes:
			votes[res] += 1
		else:
			votes[res] = 1
	sortedVotes = sorted(votes.items(), key=operator.itemgetter(1), reverse=True)
	return sortedVotes[0][0]

def getAccuracy(testData, predicts):
	right = 0
	for x in range(len(testData)):
		if testData[x][-1] == predicts[x]:
			right += 1
	return (right/float(len(testData))) * 100.0
	
def main():
	# preparation of data
	trainingData=[]
	testData=[]
	split = 0.80
	uploadDataset('./dataset/normalised_maxmin.data', split, trainingData, testData)
	print('Training Dataset: ' + repr(len(trainingData)))
	print('Test Dataset: ' + repr(len(testData)))
	# get predictions
	predicts=[]
	i = 6
	for x in range(len(testData)):
		neighbors = getNeighbors(trainingData, testData[x], i)
		resultData = getResponse(neighbors)
		predicts.append(resultData)
		print('> predicted=' + repr(resultData) + ', actual=' + repr(testData[x][-1]))
	accuracy = getAccuracy(testData, predicts)
	print('Data Accuracy: ' + repr(accuracy) + '%')
	print('Train Dataset: ' + repr(len(trainingData)))
	print('Test Dataset: ' + repr(len(testData)))
main()
