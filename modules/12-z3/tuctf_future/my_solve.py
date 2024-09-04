#!/usr/bin/python3
from z3 import *

def genMatrix(matrix, str):
	for i in range(0,25):
		m = (i*2) % 25
		f = (i*7) % 25
		matrix[int(m/5)][f%5] = 
