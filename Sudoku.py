# -*- coding: utf-8 -*-
"""
@author: Abhay Kshirsagar
backtracking
"""

import numpy as np
import time
import sys
start_time = time.time()
sys.maxsize
puzzle = "570100904600090001090000000010400200200508009009007060000000040100050003802001090"
#if zero is in the first place directly convert it into string
a=[int(d) for d in puzzle]

sudoku = np.array(a).reshape(9,9)

'''
some examples
sudoku = np.array([9,0,0,0,0,0,1,0,0,7,0,0,0,0,9,5,3,0,3,0,0,1,0,0,4,0,0,0,0,8,3,0,4,0,0,0,0,0,0,9,0,5,0,0,0,0,0,0,7,0,1,2,0,0,0,0,2,0,0,7,0,0,5,0,7,4,6,0,0,0,0,8,0,0,9,0,0,0,0,0,1]).reshape(9,9)
sudoku = np.array([1,0,0,8,0,0,0,0,3,2,0,6,5,0,7,0,1,0,9,0,0,0,0,0,0,5,0,5,7,0,0,0,3,0,0,0,6,4,0,1,0,5,0,7,2,0,0,0,4,0,0,0,3,9,0,1,0,0,0,0,0,0,5,0,6,0,9,0,2,7,0,4,4,0,0,0,0,8,0,0,1]).reshape(9,9)
killer17 = 200700000100000000000430200000000006000509000000000418000081000002000050040000300
570100904600090001090000000010400200200508009009007060000000040100050003802001090
500371009600000001007806400003604900001000800008907200005402300700000004800759002
'''

print(sudoku)
def nextcell(sud,i,j):
    """
    for x in range(i,9):
        for y in range(j,9):
            if sud[x,y]==0:#if the next cell after the one just filled
                #print(x,y,"1 nextcell")
                return x,y
    """
    for x,y in product(range(9),repeat=2):#cell search for zero
        if sud[x,y]==0:
            #print(x,y,"2 nextcell")
            return x,y
    
    return a,-1#Base case 

def validnum(sud,i,j,num):#checks the validity of the number
    row=all([num != sud[i,x] for x in range(9)])#Return true if all x are t
    if row:
        col=all([num != sud[x,j] for x in range(9)])
        if col:
            #finding the top values of each section/block
            ux=int(i/3)*3
            uy=int(j/3)*3
            for x in range(ux,ux+3):
                for y in range(uy,uy+3):
                    if sud[x,y]==num:
                        return False
            return True
    return False #base Case
    
def solver(sud,i=0,j=0):
    #our cell search is defined as a generator in nextcell() 
    i,j=nextcell(sud,i,j)
    if i == a:#No empty cells out of the array
        return True
    for test in range(1,10):
        if validnum(sud,i,j,test):#check Whether the num is suitable
        #its the same as our possible num
            #print("Trying",test)
            sud[i,j]=test
            if solver(sud,i,j):#checking the validity of our num
             #   print(sud)
                return True
            # Now the backtracking
            sud[i,j]=0
    return False

solver(sudoku)
print(sudoku)
print("Time required:'{0}' seconds".format(time.time() - start_time))
