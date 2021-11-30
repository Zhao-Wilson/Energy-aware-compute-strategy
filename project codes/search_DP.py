from systemComfig import *
import time
from dp import *
"""
Search for the optimal strategy given energy limit
"""

def search_best_choice(dp_table,Energy_arr,Energy_limit):
    """
    By using the dp-table, we can easily search for the optimal strategy

    :param dp_table: dynamic programming table obtained from dp.py
    :param Energy_arr: original generated Energy_arr table
    :param Energy_limit: the energy constraint
    :return:
    """
    T1 = time.time()
    best_choice = []
    optimal_energy = 0
    avai = Energy_limit
    optimal_BW=0
    for k in range(1,cluster+1):
        dp_arr = dp_table.get(k)
        start = 0
        en_list = dp_arr[:,0]
        for each in range(len(en_list)):
            if en_list[each] <= avai and each + 1 < len(en_list) and en_list[each + 1] <= avai: start += 1
            if en_list[each] > avai: break
        allocation = int(dp_arr[start][-1])
        if optimal_BW == 0: optimal_BW = dp_arr[start][-2]
        best_choice.append(allocation)
        optimal_energy += Energy_arr[allocation][k-1]
        avai = Energy_limit-optimal_energy

    T2 = time.time()
    # for i in dp_table[1]:
    #     print(i)

    # print("search time is: "+str(T2-T1)+" s")

    return best_choice, optimal_energy, optimal_BW