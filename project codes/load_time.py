from dp import *
from systemComfig import *
from search_DP import *
import matplotlib.pyplot as plt
"""
This module calculates how much time need to spend in order to handle specific 
workload of 50 GBytes based on different strategy with different optimal bandwidth
"""

BW_arr,Energy_arr = generate_table()
Energy_constraint_list = np.arange(100,1200,50)
dp_table = build_dp_table(Energy_constraint_list[-1],Energy_arr,BW_arr)
data_size = 50
dp_ = [] # dynamic programming results
rr_ = [] # roundrobin results
random_=[] # random results
localFirst = [] # localfirst results

def load_random(Energy_cost,BW_arr,Energy_arr):
    """
    calculate optimal bandwidth of random strategy
    under specific energy constraint

    :param Energy_cost: energy constraint
    :param BW_arr: original bandwidth table
    :param Energy_arr: original energy cost table
    :return: optimal bandwidth
    """
    tmp_E = 0
    tmp_bw = 0
    while(tmp_E>Energy_cost or tmp_E==0):
        tmp_E = 0
        tmp_bw = 0
        for i in range(cluster):
            index = np.random.randint(low=0, high=Nodes, size=1)[0]
            if (tmp_E+Energy_arr[index, i]>Energy_cost-Energy_bound): break
            tmp_bw += BW_arr[index, i]
            tmp_E += Energy_arr[index, i]

    return tmp_bw

def round_robin(Energy_cost,BW_arr,Energy_arr):
    """
    calculate optimal bandwidth of round_robin strategy
    under specific energy constraint

    :param Energy_cost: energy constraint
    :param BW_arr: original bandwidth table
    :param Energy_arr: original energy cost table
    :return: optimal bandwidth
    """

    tmp_E = 0
    tmp_bw = 0
    level = 0
    select_list = np.zeros([cluster, ])
    out_flag = False
    for k in range(Nodes):
        for i in range(cluster):
            if tmp_E+Energy_arr[level][i] > Energy_cost:
                out_flag = True
                break
            else:
                tmp_bw += BW_arr[level][i]
                tmp_E += Energy_arr[level][i]
                if level > 0:
                    tmp_bw -= BW_arr[level - 1][i]
                    tmp_E -= Energy_arr[level - 1][i]
                    select_list[i] += 1
        if out_flag: break
        level += 1

    tmp_E = 0
    tmp_bw = 0
    for i in range(len(select_list)):
        tmp_E += Energy_arr[int(select_list[i])][i]
        tmp_bw += BW_arr[int(select_list[i])][i]

    return tmp_bw

def load_localFirst(Energy_cost,BW_arr,Energy_arr):
    """
    calculate optimal bandwidth of localFirst strategy
    under specific energy constraint

    :param Energy_cost: energy constraint
    :param BW_arr: original bandwidth table
    :param Energy_arr: original energy cost table
    :return: optimal bandwidth
    """

    tmp_E = 0
    tmp_bw = 0
    select_list = np.zeros([cluster, ])
    out_flag = False
    for j in range(cluster):
        for i in range(Nodes):
            if tmp_E+Energy_arr[i][j] > Energy_cost-Energy_bound:
                out_flag = True
                break
            else:
                select_list[j] += 1
        if out_flag: break
        tmp_bw += BW_arr[-1][j]
        tmp_E += Energy_arr[-1][j]

    tmp_E = 0
    tmp_bw = 0
    for i in range(len(select_list)):
        tmp_E += Energy_arr[int(select_list[i])][i]
        tmp_bw += BW_arr[int(select_list[i])][i]

    return tmp_bw


for j in Energy_constraint_list:
    best_choice,final_energy,high_BW = search_best_choice(j,dp_table,Energy_arr)
    dp_.append(data_size/high_BW)
    random_.append(data_size/load_random(j,BW_arr,Energy_arr))
    rr_.append(data_size/round_robin(j,BW_arr,Energy_arr))
    localFirst.append(data_size/load_localFirst(j,BW_arr,Energy_arr))


plt.title("Given different load, how much time for different energy")
plt.plot(Energy_constraint_list, dp_, color='green',label="DP with 50 GBytes")
plt.plot(Energy_constraint_list, localFirst, color='blue', label="LocalFirst with 50 GBytes")
plt.plot(Energy_constraint_list, rr_, color='skyblue',label="RoundRobin with 50 GBytes")
plt.plot(Energy_constraint_list, random_, color="red",label="Random with 50 GBytes")
plt.legend()  # draw pic
plt.xlabel('Energy constraint')
plt.ylabel('Time * 10^2 (s)')
plt.show()