#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 16:32:05 2023

@author: monikasameer
"""

import time
import matplotlib.pyplot as plt

# Naive Iterative Method
def power_iterative(a, n):
    result = 1
    for _ in range(n):
        result *= a
    return result

# Divide-and-Conquer Approach
def power_divide_and_conquer(a, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        half_power = power_divide_and_conquer(a, n // 2)
        return half_power * half_power
    else:
        half_power = power_divide_and_conquer(a, (n - 1) // 2)
        return a * half_power * half_power

# Function to measure execution time for both methods
def measure_execution_time(func, a, n):
    start_time = time.time()
    result = func(a, n)
    end_time = time.time()
    execution_time = end_time - start_time
    return execution_time

# Experiment setup
n_values = list(range(1, 10001, 100))  # Vary n from 1 to 10,000
iterative_times = []
divide_and_conquer_times = []

# Run experiments and measure execution times
for n in n_values:
    iterative_time = measure_execution_time(power_iterative, 2, n)
    divide_and_conquer_time = measure_execution_time(power_divide_and_conquer, 2, n)
    iterative_times.append(iterative_time)
    divide_and_conquer_times.append(divide_and_conquer_time)

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(n_values, iterative_times, label='Iterative Method', marker='o')
plt.plot(n_values, divide_and_conquer_times, label='Divide and Conquer', marker='o')
plt.xlabel('n')
plt.ylabel('Execution Time (s)')
plt.legend()
plt.grid(True)
plt.title('Algorithm Scalability Comparison')
plt.show()