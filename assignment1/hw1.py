#
# CS 196 Data Hackerspace
# Assignment 1: Data Parsing and NumPy
# Due October 1st, 2018
#

import json
import csv
import numpy as np
import pandas as pd

def histogram_times(filename):
	import re
	my_csv = pd.read_csv(filename)
	np_csv = my_csv.values
	frequency = []
	for i in range(24):
		frequency.append(0)
	nan = np_csv[2,1]
	times = np_csv[:, 1]
	times = filter(lambda v: v==v, times)
	for time in times:
		time = time[0:len(time) - 2]
		arr = re.findall('\d+', time)
		for num in arr:
			if num != '' and len(num) <= 2:
				frequency[int(num)] += 1
	return frequency


def weigh_pokemons(filename, weight):
    jso = pd.read_json(filename)
    return_list = []
    for dic in jso['pokemon']:
    	if(dic["weight"] == str(weight) + ' kg'):
    		return_list.append(dic['name'])
    return return_list

def single_type_candy_count(filename):
    jso = pd.read_json(filename)
    counter = 0
    for dic in jso['pokemon']:
    	if(len(dic["type"]) == 1 and 'candy_count' in dic):
    		counter += (dic['candy_count'])
    return counter

def reflections_and_projections(points):
	trans_matrix1 = [[1, 0], [0, -1]]
	trans_matrix2 = [[0, -1], [1, 0]]
	trans_matrix3 = [[1, 0.3], [0.3, 0.9]]
	return_matrix = np.matmul(trans_matrix1, points)
	return_matrix[1] += 2
	return_matrix = np.matmul(trans_matrix2, points)
	return_matrix = np.matmul(trans_matrix3, points)
	return return_matrix

def normalize(image):
	min_val = np.amin(image)
	max_val = np.amax(image)
	coeff = 255 / (max_val - min_val)
	return_matrix = []
	for vec in image:
		temp = []
		for num in vec:
			temp.append(coeff * (num - min_val))
		return_matrix.append(temp)
	return return_matrix	

def sigmoid_normalize(image, a):
    return_matrix = []
    for vec in image:
    	temp = []
    	for num in vec:
    		exp = ((num - 128) * (a ** -1) * (-1))
    		base = 1 + (e ** exp)
    		temp.append(255 * (base ** -1))
    	return_matrix.append(temp)
    return return_matrix






