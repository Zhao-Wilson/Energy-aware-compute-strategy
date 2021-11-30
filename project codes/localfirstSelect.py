from systemComfig import *
import numpy as np
"""
This module use localfirst strategy to find relationship between number of nodes and Energy cost
as well as number of nodes and bandwidth
"""

def cluster_localfirst(optimal_BW,optimal_energy,BW_arr,Energy_arr):
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
    tmp_E = 0
    tmp_bw = 0
    select_list = np.zeros([cluster, ])
    out_flag = False
    for j in range(cluster):
        for i in range(Nodes):
            if tmp_bw + BW_arr[i][j] > optimal_BW + BW_bound:
                out_flag = True
                break
            else:
                select_list[j] += 1
        if out_flag: break
        tmp_bw += BW_arr[-1][j]


    for i in range(len(select_list)):
        tmp_E += Energy_arr[int(select_list[i])][i]
        tmp_n += select_list[i]

    results.append(tmp_n)
    results.append(tmp_E)
    # print("RR- 1) fixed B, find n,E: bw=%.2f" % tmp_bw + ", E %.2f" % tmp_E + ", n %d" % tmp_n)

    # 1) fixed E, find n,bw
    tmp_n = 0
    tmp_E = 0
    tmp_bw = 0
    select_list = np.zeros([cluster, ])
    out_flag = False
    for j in range(cluster):
        for i in range(Nodes):
            if tmp_E + Energy_arr[i][j] > optimal_energy+Energy_bound:
                out_flag = True
                break
            else:
                select_list[j] += 1
        if out_flag: break
        tmp_E += Energy_arr[-1][j]

    for i in range(len(select_list)):
        tmp_bw += BW_arr[int(select_list[i])][i]
        tmp_n += select_list[i]

    results.append(tmp_n)
    results.append(tmp_bw)
    # print("range- 2) fixed E, find n,BW: E=%.2f" % tmp_E + ", bw %.2f" % tmp_bw + ", n %d" % tmp_n)

    return results