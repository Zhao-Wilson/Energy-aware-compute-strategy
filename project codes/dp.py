from generateNodes import *
from systemComfig import *
import time

"""
This module builds up the dynaymic programming table

The procedure consists of sorting Energy cost and building table
In order to test the module function, I provide two methods generating
original data(Bandwidth & Energy arr)
  1. randomly generate data table using from generateNodes import generate_table()
  2. handwritten data table shown below
"""

# Obtain bandwidth & energy arr using generate_table() function
BW_arr, Energy_arr = generate_table()

# handwritten data table
# BW_arr = np.zeros([4,3])
# Energy_arr = np.zeros([4,3])
# Energy_limit=300

# # initialize data
# BW_arr[1][0] = 0.5
# BW_arr[1][1] = 0.65
# BW_arr[1][2] = 0.6
# BW_arr[2][0] = 0.6
# BW_arr[2][1] = 0.7
# BW_arr[2][2] = 0.7
# BW_arr[3][0] = 0.75
# BW_arr[3][1] = 0.8
# BW_arr[3][2] = 0.8

# Energy_arr[1][0] = 100
# Energy_arr[1][1] = 80
# Energy_arr[1][2] = 95
# Energy_arr[2][0] = 110
# Energy_arr[2][1] = 85
# Energy_arr[2][2] = 100
# Energy_arr[3][0] = 125
# Energy_arr[3][1] = 90
# Energy_arr[3][2] = 110

# get energy interval list

# initialize data
# BW_arr[1][0] = 1.4
# BW_arr[1][1] = 1.6
# BW_arr[1][2] = 1.9
# BW_arr[2][0] = 2.1
# BW_arr[2][1] = 2.4
# BW_arr[2][2] = 2.5
# BW_arr[3][0] = 2.8
# BW_arr[3][1] = 3.1
# BW_arr[3][2] = 3.0
#
# Energy_arr[1][0] = 75
# Energy_arr[1][1] = 80
# Energy_arr[1][2] = 90
# Energy_arr[2][0] = 95
# Energy_arr[2][1] = 95
# Energy_arr[2][2] = 95
# Energy_arr[3][0] = 100
# Energy_arr[3][1] = 105
# Energy_arr[3][2] = 110

def Energy_interval(Energy_arr,clu,Energy_limit):
    """
    Use Cartesian Product to generate Energy cost array and sort them
    based on Energy_arr, cluster index and Energy_limit

    :param Energy_arr: original generated Energy_arr table
    :param clu: indicate current loop is in which cluster
    :param Energy_limit: the energy constraint
    :return: sorted Energy cost in a list
    """
    Energy_list = []
    for i in range(cluster, clu - 1, -1):
        if i != cluster:
            size = len(Energy_list)
            for s in range(size):
                for j in range(Nodes+1):
                    sum_ = Energy_arr[j][i - 1] + Energy_list[s]
                    if sum_ not in Energy_list and sum_ <= Energy_limit:
                        Energy_list.append(sum_)

        else:
            for j in range(Nodes+1):
                if Energy_arr[j][i - 1] not in Energy_list and Energy_arr[j][i - 1] <= Energy_limit:
                    Energy_list.append(Energy_arr[j][i - 1])

    Energy_list.sort()
    return Energy_list


# build DP table
dp_table = {}
def build_dp_table(Energy_arr,BW_arr,Energy_limit):
    """
    transverse every node number to search for the original Energy table
    and then using the remaining energy to search for last phase table
    to save time

    :param Energy_limit: the energy constraint
    :param Energy_arr: original generated Energy_arr table
    :param BW_arr: original generated Bandwodth_arr table
    :return: global dynamic programming table of all the clusters
    """
    for k in range(cluster,0,-1):
        T1 = time.time()
        # sort Energy list
        Energy_list = Energy_interval(Energy_arr,k,Energy_limit)
        dp_arr = np.zeros([len(Energy_list),4+Nodes])

        for en in range(len(Energy_list)): #transverse every energy cost
            for machine in range(Nodes+1): #transverse every node
                bw_acc = 0
                avai_enr = Energy_list[en]
                if Energy_arr[machine][k-1]<=avai_enr: #judge whether smaller than current available energy
                    bw_acc+=BW_arr[machine][k-1]
                    avai_enr-=Energy_arr[machine][k-1]
                    last_arr = dp_table.get(k+1) #obtain last phase(cluster) dp-table
                    if last_arr is not None:
                        en_list = last_arr[:,0]
                        start = 0
                        for each in range(len(en_list)): #locate the energy index in the last phase dp-table
                            if en_list[each]<=avai_enr and each+1<len(en_list) and en_list[each+1]<=avai_enr: start+=1
                            if en_list[each]>avai_enr: break
                        bw_acc+=last_arr[start][-2]
                        tmp_machine = int(last_arr[start][-1])
                        avai_enr-=Energy_arr[tmp_machine][k-1]
                    dp_arr[en][machine+1] = bw_acc
                else: break
            index = dp_arr[en][1:Nodes+2].argmax() #choose the optimal number of nodes
            dp_arr[en][0] = Energy_list[en]
            dp_arr[en][-2] = dp_arr[en][index+1]
            dp_arr[en][-1] = index
        dp_table[k] = dp_arr
        T2 = time.time()
        # print("k="+str(k)+"build table time is: " + str(T2-T1) + " s")

    return dp_table
