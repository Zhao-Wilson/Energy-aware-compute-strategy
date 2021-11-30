import numpy as np
from systemComfig import *
"""
This module use roundrobin strategy to find relationship between number of nodes and Energy cost
as well as number of nodes and bandwidth
"""

def cluster_roundrobin(optimal_BW,optimal_energy,BW_arr,Energy_arr):
    results = []
    """
    This first port is to fix bandwidth to find the relation between n and E
    The second part is to fix Energy to find the relation between n and BW

    :param optimal_BW: optimal bandwidth obtained from dp method
    :param optimal_energy: optimal energy obtained from dp method
    :param BW_arr: original generated bandwidth_arr table
    :param Energy_arr: original generated Energy_arr table
    :return: results
    """

    # 1) fixed B, find n,E
    tmp_n = 0
    tmp_E = 0
    tmp_bw=0
    level = 0
    select_list = np.zeros([cluster,])
    out_flag=False
    for k in range(Nodes):
        tmp_bw = 0
        for i in range(cluster):
            if tmp_bw + BW_arr[level][i] > optimal_BW + BW_bound:
                out_flag = True
                break
            else:
                tmp_bw += BW_arr[level][i]
                select_list[i]+=1
        if out_flag: break
        level+=1

    for i in range(len(select_list)):
        tmp_E+=Energy_arr[int(select_list[i])][i]
        tmp_n+=select_list[i]


    results.append(tmp_n)
    results.append(tmp_E)
    # print("range- 1) fixed B, find n,E: bw=%.2f"%tmp_bw+", E %.2f"%tmp_E+", n %d"%tmp_n)

    # 1) fixed E, find n,bw
    tmp_n = 0
    tmp_E = 0
    tmp_bw = 0
    level = 0
    select_list = np.zeros([cluster, ])
    out_flag = False
    for k in range(Nodes):
        tmp_E = 0
        for i in range(cluster):
            if tmp_E + Energy_arr[level][i] > optimal_energy+Energy_bound:
                out_flag = True
                break
            else:
                tmp_E += Energy_arr[level][i]
                select_list[i] += 1
        if out_flag: break
        level += 1

    for i in range(len(select_list)):
        tmp_bw += BW_arr[int(select_list[i])][i]
        tmp_n += select_list[i]

    results.append(tmp_n)
    results.append(tmp_bw)
    # print("range- 2) fixed E, find n,BW: E=%.2f"%tmp_E+", bw %.2f"%tmp_bw+", n %d"%tmp_n)

    return results
