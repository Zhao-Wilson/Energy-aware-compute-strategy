from dp import *
from systemComfig import *
from randomSelect import *
from roundrobinSelect import *
from localfirstSelect import *
from search_DP import *
"""
This module compare the four strategies with similar bandwidth 
and energy cost to find how many workers need
"""

dp_E_B = []
rand_E_B = []
rang_E_B = []
rr_E_B = []

BW_arr,Energy_arr = generate_table()
Energy_constraint_list = np.arange(100,1200,50)
dp_table = build_dp_table(Energy_constraint_list[-1],Energy_arr,BW_arr)

def table_random(optimal_BW,optimal_Energy,BW_arr,Energy_arr):
    # 1) fixed B，E, find n
    tmp_n = 0
    tmp_bw = 0
    tmp_E = 0
    while np.abs(tmp_bw - optimal_BW) > BW_bound * 2 or np.abs(tmp_E-optimal_Energy) > Energy_bound*2:
        tmp_n = 0
        tmp_bw = 0
        tmp_E = 0
        for i in range(cluster):
            index = np.random.randint(low=0, high=Nodes, size=1)[0]
            if (BW_arr[index, i] > optimal_BW + BW_bound or Energy_arr[index,i]>optimal_Energy+Energy_bound):
                for j in range(index - 1, -1, -1):
                    if BW_arr[j, i] < optimal_BW + BW_bound and Energy_arr[index,i] < optimal_Energy+Energy_bound:
                        tmp_n += j
                        tmp_bw += BW_arr[j, i]
                        tmp_E += Energy_arr[j, i]
                        break
                break
            else:
                tmp_n += index
                tmp_bw += BW_arr[index, i]
                tmp_E += Energy_arr[index, i]
                if np.abs(optimal_BW - tmp_bw) <= BW_bound:
                    break

    print("random E: "+str(tmp_E)+" ,B: "+str(tmp_bw)+", n: "+str(tmp_n))

    rand_E_B.append(tmp_n)



def table_roundrobin(optimal_BW,optimal_Energy,BW_arr,Energy_arr):
    # 1) fixed B，E, find n
    tmp_n = 0
    tmp_E = 0
    tmp_bw = 0
    level = 0
    select_list = np.zeros([cluster, ])
    out_flag = False
    for k in range(Nodes):
        for i in range(cluster):
            if tmp_bw + BW_arr[level][i] > optimal_BW+BW_bound*2 and tmp_E+Energy_arr[level][i] > optimal_Energy+Energy_bound*2:
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
        tmp_n += int(select_list[i])
        tmp_bw += BW_arr[int(select_list[i])][i]


    print("range E: "+str(tmp_E)+" ,B: "+str(tmp_bw)+", n: "+str(tmp_n))

    rang_E_B.append(tmp_n)


def table_localfirst(optimal_BW,optimal_Energy,BW_arr,Energy_arr):
    # 1) fixed B，E, find n
    tmp_n = 0
    tmp_E = 0
    tmp_bw = 0
    select_list = np.zeros([cluster, ])
    out_flag = False
    for j in range(cluster):
        for i in range(Nodes):
            if tmp_bw + BW_arr[i][j] > optimal_BW + BW_bound or tmp_E+Energy_arr[i][j] > optimal_Energy + Energy_bound:
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
        tmp_n += int(select_list[i])
        tmp_bw += BW_arr[int(select_list[i])][i]

    print("rr E: "+str(tmp_E)+" ,B: "+str(tmp_bw)+", n: "+str(tmp_n))

    rr_E_B.append(tmp_n)


for EC in Energy_constraint_list:
    best_choice,optimal_Energy,optimal_BW = search_best_choice(EC,dp_table,Energy_arr)
    dp_E_B.append(sum(best_choice))
    print("dp E: "+str(optimal_Energy)+", B: "+str(optimal_BW)+", n: "+str(sum(best_choice)))

    table_random(sum(best_choice),optimal_BW,optimal_Energy,BW_arr)
    table_roundrobin(sum(best_choice),optimal_BW,optimal_Energy,BW_arr)
    table_localfirst(sum(best_choice),optimal_BW,optimal_Energy,BW_arr)

    print("============")


print(dp_E_B)
print(rand_E_B)
print(rang_E_B)
print(rr_E_B)