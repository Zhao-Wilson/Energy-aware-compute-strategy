import numpy as np
from systemComfig import *
"""
This module use random strategy to find relationship between number of nodes and Energy cost
as well as number of nodes and bandwidth
"""

def cluster_random(optimal_BW,optimal_energy,BW_arr,Energy_arr):
    """
    This first port is to fix bandwidth to find the relation between n and E
    The second part is to fix Energy to find the relation between n and BW

    :param optimal_BW: optimal bandwidth obtained from dp method
    :param optimal_energy: optimal energy obtained from dp method
    :param BW_arr: original generated bandwidth_arr table
    :param Energy_arr: original generated Energy_arr table
    :return: results
    """
    results = []

    # 1) fixed B, find n,E
    tmp_n = 0
    tmp_bw = 0
    tmp_E = 0
    # if the difference between current bandwidth and optimal bandwidth
    # is too much bigger need to try it again
    while np.abs(tmp_bw-optimal_BW) > BW_bound*2:
        tmp_n = 0
        tmp_bw = 0
        tmp_E = 0
        for i in range(cluster):
            index = np.random.randint(low=0,high=Nodes,size=1)[0]
            if BW_arr[index,i] > optimal_BW + BW_bound:
                for j in range(index - 1, -1, -1):
                    if BW_arr[j,i] < optimal_BW + BW_bound: # decrease the search range
                        tmp_n += j
                        tmp_bw += BW_arr[j,i]
                        tmp_E += Energy_arr[j,i]
                        break
                break
            else:
                tmp_n += index
                tmp_bw += BW_arr[index,i]
                tmp_E += Energy_arr[index,i]
                if np.abs(optimal_BW-tmp_bw)<=BW_bound:
                    break
    results.append(tmp_n)
    results.append(tmp_E)
    # print("random- 1) fixed B, find n,E: bw=%.2f"%tmp_bw+", E %.2f"%tmp_E+", n %d"%tmp_n)

    # 2) fixed E, find n,BW
    tmp_n = 0
    tmp_bw = 0
    tmp_E = 0
    while np.abs(tmp_E-optimal_energy) > Energy_bound:
        tmp_n = 0
        tmp_bw = 0
        tmp_E = 0
        for i in range(cluster):
            index = np.random.randint(low=0, high=Nodes, size=1)[0]
            if Energy_arr[index,i] > optimal_energy + Energy_bound:
                for j in range(index - 1, -1, -1):
                    if Energy_arr[j,i] < optimal_energy + Energy_bound:
                        tmp_n += j
                        tmp_bw += BW_arr[j,i]
                        tmp_E += Energy_arr[j,i]
                        break
                break
            else:
                tmp_n += index
                tmp_bw += BW_arr[index,i]
                tmp_E += Energy_arr[index,i]
                if np.abs(optimal_energy - tmp_E) <= Energy_bound:
                    break
    results.append(tmp_n)
    results.append(tmp_bw)
    # print("random- 2) fixed E, find n,BW: E=%.2f"%tmp_E+", bw %.2f"%tmp_bw+", n %d"%tmp_n)

    return results
