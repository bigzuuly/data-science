'''
Created on Dec 13, 2016

@author: ThomasC
'''

def shape(A):
    num_rows = len(A)
    num_cols = len(A[0])
    
    return num_rows, num_cols

def get_row(A, i):
    return A[i]

def get_column(A, j):
    return [A_i[j] for A_i in A]

def make_matrix(num_rows, num_cols, entry_fn):
    return [[entry_fn(i, j)
              for j in range(num_cols)]
            for i in range(num_rows)]
    
def is_diagonal(i, j):
    if i == j:
        return 1
    else:
        return 0
    
identity_matrix = make_matrix(5, 5, is_diagonal)

def print_matrix(A):
    for row in A:
        print (row)


print_matrix(identity_matrix)