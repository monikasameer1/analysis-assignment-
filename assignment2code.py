#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 14:25:12 2023

@author: monikasameer
"""

def highest_scoring_alignment(x, y, scoringmatrix):
    n = len(x)
    m = len(y)

    # Initialize the DP matrix
    dynamicmat = [[0] * (m + 1) for _ in range(n + 1)]

    # Fill in the DP matrix
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            match = dynamicmat[i - 1][j - 1] + scoringmatrix[x[i - 1]][y[j - 1]]
            delete = dynamicmat[i - 1][j] + scoringmatrix[x[i - 1]]['-']
            insert = dynamicmat[i][j - 1] + scoringmatrix['-'][y[j - 1]]
            dynamicmat[i][j] = max(match, delete, insert)

    # Traceback to reconstruct the alignment
    alignx, aligny = '', ''
    i, j = n, m
    while i > 0 or j > 0:
        if i > 0 and j > 0 and dynamicmat[i][j] == dynamicmat[i - 1][j - 1] + scoringmatrix[x[i - 1]][y[j - 1]]:
            alignx = x[i - 1] + alignx
            aligny = y[j - 1] + aligny
            i -= 1
            j -= 1
        elif i > 0 and dynamicmat[i][j] == dynamicmat[i - 1][j] + scoringmatrix[x[i - 1]]['-']:
            alignx = x[i - 1] + alignx
            aligny = '-' + aligny
            i -= 1
        else:
            alignx = '-' + alignx
            aligny = y[j - 1] + aligny
            j -= 1

    return alignx, aligny

# Scoring matrix
scoringmatrix = {
    'A': {'A': 1, 'G': -0.8, 'T': -0.2, 'C': -2.3, '-': -0.6},
    'G': {'A': -0.8, 'G': 1, 'T': -1.1, 'C': -0.7, '-': -1.5},
    'T': {'A': -0.2, 'G': -1.1, 'T': 1, 'C': -0.5, '-': -0.9},
    'C': {'A': -2.3, 'G': -0.7, 'T': -0.5, 'C': 1, '-': -1},
    '-': {'A': -0.6, 'G': -1.5, 'T': -0.9, 'C': -1, '-': float('-inf')}
}

# Gene sequences
genex = "TCCCAGTTATGTCAGGGGACACGAGCATGCAGAGAC"
geney = "AATTGCCGCCGTCGTTTTCAGCAGTTATGTCAGATC"

# Calculate the highest-scoring alignment
alignmentx, alignmenty = highest_scoring_alignment(genex, geney, scoringmatrix)

# Print the results
print("Gene X:", alignmentx)
print("Gene Y:", alignmenty)


