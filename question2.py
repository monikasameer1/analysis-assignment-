#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 16:53:52 2023

@author: monikasameer
"""

import time
import random
import matplotlib.pyplot as plt

def binary_search(arr, x):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return True
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return False

def merge_sort(arraylist):
    if len(arraylist) > 1:
        middle = len(arraylist) // 2
        left = arraylist[:middle]
        right = arraylist[middle:]

        merge_sort(left)
        merge_sort(right)

        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arraylist[k] = left[i]
                i += 1
            else:
                arraylist[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arraylist[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arraylist[k] = right[j]
            j += 1
            k += 1


def find_pairs_with_sum(S, target):
    pairs = []
    merge_sort(S)
    for i in range(len(S)):
        complement = target - S[i]
        if binary_search(S, complement) and complement not in pairs:
            pairs.append((S[i], complement))
    return pairs



n_values = list(range(1, 10001, 100))  
execution_times = []
target = 15  

for n in n_values:
    S = [random.randint(1, 1000) for _ in range(n)]  

   
    start_time = time.time()
    find_pairs_with_sum(S, target)
    end_time = time.time()

    execution_time = end_time - start_time
    execution_times.append(execution_time)


plt.figure(figsize=(10, 6))
plt.plot(n_values, execution_times, label='Execution Time', marker='o')
plt.xlabel('n')
plt.ylabel('Execution Time (s)')
plt.grid(True)
plt.title('Algorithm Scalability')
plt.show()
