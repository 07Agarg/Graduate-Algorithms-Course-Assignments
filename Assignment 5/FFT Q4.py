# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 15:08:49 2020

@author: Ashima
"""

import numpy as np
import more_itertools

def MakeList(a):
    if len(a) <= 1:
        return a
    A_E = ""
    A_O = ""
    for i in range(len(a)):
        if i % 2 == 0:
            A_E = A_E + a[i]
        else:
            A_O = A_O + a[i]
    a_e = MakeList(A_E)
    a_o = MakeList(A_O)
    return [a_e, a_o]


def MakeListHelper(a, n):
    if len(a) <= 1:
        return a
    even_list = []
    # A_E = ""
    # A_O = ""
    for i in range(len(a)):
        if i % 2 == 0:
            even_list.append(i)
    # print("even_list: ", even_list)
    a_e = MakeListHelper(even_list, n)
    a_e = list(more_itertools.collapse(a_e))
    a_o = np.add(even_list, 1).tolist()
    # print("a_e: ", a_e)
    # print("a_o: ", a_o)
    # print("2*a_e: ", np.multiply(a_e, 2))
    # print("2*a_o: ", np.multiply(a_o, 2))
    # print(len(a_e))
    if (len(a_e) < n/2): 
        # print("executed")
        # print("a_e now, len(a_e), n/2: ", a_e, len(a_e))
        a_e = np.multiply(a_e, 2).tolist()
        a_o = np.multiply(a_o, 2).tolist()
    # else:
        # print("not executed")
    return [a_e, a_o]


def MakeList(a):
    a_final = ""
    # final_indices = MakeListHelper([0, 1, 2, 3], 4)
    final_indices = MakeListHelper([0, 1, 2, 3, 4, 5, 6, 7], 8)
    # final_indices = MakeListHelper([0], 8)
    print(final_indices)
    final_indices = list(more_itertools.collapse(final_indices))
    # convert_to_list()
    for i in final_indices:
        print(a[i], end="")

# MakeList("ABCD")
MakeList("ABCDEFGH")
# print(MakeList("BUTTERFLYNETWORK"))