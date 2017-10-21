
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 14:58:36 2017

@author: micsh
"""

### 1. Linear Search ###
def linearSearch(F, target):
    for x in range(len(F)):
        if (F[x] == target):
            return x
    return False

F1 = (9, 8, 3, 4, 64, 5)
t1 = 5
print "1. Linear Search: Looking for the index of {} in array {}".format(t1, F1)
print linearSearch(F1, t1)



### 2. Exhaustive Enumeration ###
def linearSearch_sqrt(N):
    epsilon = 0.001
    x = 0.000
    while x*x < N-epsilon:
        x += epsilon
    return x

N2 = 99999
print "2. Linear Search Square Root: Looking for the square root of {}".format(N2)
print linearSearch_sqrt(N2)

# cross check against function above
# from math import sqrt
# print sqrt(N2)



### 3. Binary Search ###
def binarySearch(A, target):
    low = 0
    high = len(A) - 1
    idx = False

    while low < high and not idx:
        mid = (low + high) / 2
#        mid = low + (high - low) /2
#        print "LOW {} HI {} MID {}, comparing {} to {}".format(low, high, mid, target, A[mid])
        if A[mid] == target:
            return mid
        if A[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return False

A3 = range(7)
t3 = 3
print "3. Binary Search: Looking for the index of {} in array {}".format(t3, A3)
print binarySearch(A3, t3)



### 5. Finding a Square Root ###
""" Modify binary search to create a function, bisection search nth root(N,k), that
calculates f(N, k) = sqrt(N, k) within E = 0.001"""

def bisection_search_kth_root(N, k):
    epsilon = 0.001
    low = 0
    high = 10000
#    i = 0
    idx = False
    while low < high and not idx:
        mid = (low + high) / 2
#        i += 1
#        print "LOW {} HI {} MID {}, comparing {} to {}".format(low, high, mid, N, mid**k)
        if mid**k == N - epsilon:
            return mid
        if mid**k < N - epsilon:
            low = mid + epsilon
        else:
            high = mid - epsilon
    return mid#, i

N5 = 125
k5 = 3
print "5. Bisection Search: Looking for {}th square root for {}".format(k5, N5)
print bisection_search_kth_root(N5, k5)



### 7. Argmax Constraint ###
from math import log
def bisection_search_lgN(N):
    epsilon = 0.001
    low = 0
    high = 0.001
    idx = False
    while high * log(high, 2) - high + 1 < N:
        high = high * 2

    while high - low > epsilon and not idx:
        mid = float((low + high)) / 2
#        chk = mid * log(mid,2) - mid + 1
#        print "LOW {} HI {} MID {}, comparing {} to {}".format(low, high, mid, N, mid * log(mid,2) - mid + 1)
        if mid * log(mid, 2) - mid + 1 == N - epsilon:
            return mid
        if mid * log(mid, 2) - mid + 1 > N - epsilon:
            high = mid
        else:
            low = mid
    return mid

N = 2**43
print "7. Bisection Search of Log(N!): Looking for the maximal N whose factorial could be computed and stored on the laptop with 1TB of space"
print bisection_search_lgN(N)



### 8. Newton-Raphson ###
def newton_sqrt(k):
    epsilon = .001
    y = k / 2.0 #guess
    while abs(y * y - k) >= epsilon:
        y = y - (((y**2) - k) / (2 * y))
    return y

N8 = 99999
print "8. Newton Raphson Square Root: Looking for square root of {} using Newton-Raphson approach".format(N8)
print newton_sqrt(N8)
