'''
Created on Dec 13, 2016

@author: ThomasC
'''

import math
from functools import reduce

def vector_add(v, w):
    return [v_i + w_i for v_i, w_i in zip(v,w)]

def vector_subtract(v, w):
    return [v_i - w_i for v_i, w_i in zip(v,w)]

def vector_sum(vectors):
    return reduce(vector_add, vectors)


def scalar_multiply(c, v):
    return [c * v_i for v_i in v]

def vector_mean(vectors):
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))

def dot(v, w):
    """v_1*w_1 + v_2*w_2 ... v_n*w_n"""
    return sum(v_i * w_i for v_i,w_i in zip(v,w))

def sum_of_squares(v):
    return dot(v,v)

def magnitude(v):
    return math.sqrt(sum_of_squares(v))

def distance(v, w):
    return magnitude(vector_subtract(v, w))
