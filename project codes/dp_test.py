import numpy as np
BW_arr = np.zeros([4,3])
Energy_arr = np.zeros([4,3])
Energy_limit=300

# initialize data
BW_arr[1][0] = 0.5
BW_arr[1][1] = 0.65
BW_arr[1][2] = 0.6
BW_arr[2][0] = 0.6
BW_arr[2][1] = 0.7
BW_arr[2][2] = 0.7
BW_arr[3][0] = 0.75
BW_arr[3][1] = 0.8
BW_arr[3][2] = 0.8

Energy_arr[1][0] = 100
Energy_arr[1][1] = 80
Energy_arr[1][2] = 95
Energy_arr[2][0] = 110
Energy_arr[2][1] = 85
Energy_arr[2][2] = 100
Energy_arr[3][0] = 125
Energy_arr[3][1] = 90
Energy_arr[3][2] = 110

# return sorted energy constraint list
def sort_Energy(enr_arr,k):
    Energy_list = []
    for i in range(3,k-1,-1):
        if i!=3:
            size = len(Energy_list)
            for s in range(size):
                for j in range(4):
                    sum_ = Energy_arr[j][i-1]+Energy_list[s]
                    if sum_ not in Energy_list and sum_<=Energy_limit:
                        Energy_list.append(sum_)

        else:
            for j in range(4):
                if Energy_arr[j][i-1] not in Energy_list and Energy_arr[j][i-1]<=Energy_limit:
                    Energy_list.append(Energy_arr[j][i-1])

    Energy_list.sort()
    return Energy_list

#build DP table
# print(sort_Energy(Energy_arr,1))
dp_table = {}
for k in range(3,0,-1):
    Energy_list = sort_Energy(Energy_arr,k)
    dp_arr = np.zeros([len(Energy_list),7])
    for en in range(len(Energy_list)):
        for machine in range(4):
            bw_acc = 0
            avai_enr = Energy_list[en]
            if Energy_arr[machine][k-1]<=avai_enr:
                bw_acc+=BW_arr[machine][k-1]
                avai_enr-=Energy_arr[machine][k-1]
                last_arr = dp_table.get(k+1)
                if last_arr is not None:
                    en_list = last_arr[:,0]
                    start = 0
                    for each in range(len(en_list)):
                        if en_list[each]<=avai_enr and each+1<len(en_list) and en_list[each+1]<=avai_enr: start+=1
                        if en_list[each]>avai_enr: break
                    bw_acc+=last_arr[start][5]
                    tmp_machine = int(last_arr[start][6])
                    avai_enr-=Energy_arr[tmp_machine][k-1]
                dp_arr[en][machine+1] = bw_acc
            else : break
        index = dp_arr[en][1:5].argmax()
        dp_arr[en][0] = Energy_list[en]
        dp_arr[en][5] = dp_arr[en][index+1]
        dp_arr[en][6] = index
    dp_table[k] = dp_arr

for i in dp_table[2]:
    print(i)

# Search best strategy given energy limit
def search_best_choice(E_limit):
    best_choice = []
    final_energy = 0
    avai = E_limit
    for k in range(1,4):
        dp_arr = dp_table.get(k)
        start = 0
        en_list = dp_arr[:,0]
        for each in range(len(en_list)):
            if en_list[each] <= avai and each + 1 < len(en_list) and en_list[each + 1] <= avai: start += 1
            if en_list[each] > avai: break
        allocation = int(dp_arr[start][6])
        best_choice.append(allocation)
        final_energy+=Energy_arr[allocation][k-1]
        avai=E_limit-final_energy
    print(best_choice)
    print(final_energy)



search_best_choice(300)