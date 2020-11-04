# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 16:40:23 2020

@author: Ashima
"""

# Python3 program to count number of times  
# S appears as a subsequence in T 
def findSubsequenceCount(S, T): 
  
    m = len(T) 
    n = len(S) 
  
    # T can't appear as a subsequence in S 
    if m > n: 
        return 0
  
    # mat[i][j] stores the count of  
    # occurrences of T(1..i) in S(1..j). 
    mat = [[0 for _ in range(n + 1)] 
              for __ in range(m + 1)] 
  
    # Initializing first column with all 0s. x 
    # An empty string can't have another 
    # string as suhsequence 
    for i in range(1, m + 1): 
        mat[i][0] = 0
  
    # Initializing first row with all 1s.  
    # An empty string is subsequence of all. 
    for j in range(n + 1): 
        mat[0][j] = 1
  
    # Fill mat[][] in bottom up manner 
    for i in range(1, m + 1): 
        for j in range(1, n + 1): 
  
            # If last characters don't match,  
            # then value is same as the value  
            # without last character in S. 
            if T[i - 1] != S[j - 1]: 
                mat[i][j] = mat[i][j - 1] 
                  
            # Else value is obtained considering two cases. 
            # a) All substrings without last character in S 
            # b) All substrings without last characters in 
            # both. 
            else:
                # mat[i][j] = 1 + (mat[i][j - 1]) 
                # mat[i][j] = max(mat[i][j - 1], mat[i - 1][j - 1]) 
                mat[i][j] = (mat[i][j - 1] + 
                              mat[i - 1][j - 1]) 
    print(mat)
    return mat[m][n] 
  
# Driver Code 
if __name__ == "__main__": 
    T = "ge"
    S = "geeksforgeeks"
    # T = "ab"
    # S = "abacbd"
    # T = "PPAP"
    # S = "PENPINEAPPLEAPPLEPEN"
    print(findSubsequenceCount(S, T)) 