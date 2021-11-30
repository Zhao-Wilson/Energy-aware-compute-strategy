from dp import *
from systemComfig import *
from randomSelect import *
from roundrobinSelect import *
from localfirstSelect import *
from search_DP import *
import matplotlib.pyplot as plt

dp_B_n = []
dp_B_E = []
dp_E_n = []
dp_E_B = []
rand_B_n = []
rand_B_E = []
rand_E_n = []
rand_E_B = []
rang_B_n = []
rang_B_E = []
rang_E_n = []
rang_E_B = []
rr_B_n = []
rr_B_E = []
rr_E_n = []
rr_E_B = []

BW_arr,Energy_arr = generate_table()
Energy_constraint_list = np.arange(100,1200,50)
dp_table = build_dp_table(Energy_constraint_list[-1],Energy_arr,BW_arr)
for EC in Energy_constraint_list:
    best_choice,final_energy,highBW = search_best_choice(EC,dp_table,Energy_arr)
    # print("DP Energy cost: %d"%EC+", DP best choice:" +str(best_choice)+", DP final_energy:" +str(final_energy)+", bw is: "+str(highBW))

    dp_B_n.append(sum(best_choice))
    dp_B_E.append(final_energy)
    dp_E_n.append(sum(best_choice))
    dp_E_B.append(highBW)

    rand_ = cluster_random(sum(best_choice), highBW, final_energy, BW_arr)
    rang_ = cluster_roundrobin(sum(best_choice),highBW,final_energy,BW_arr)
    RR_ = cluster_localfirst(sum(best_choice),highBW,final_energy,BW_arr)

    rand_B_n.append(rand_[0])
    rand_B_E.append(rand_[1])
    rand_E_n.append(rand_[2])
    rand_E_B.append(rand_[3])
    rang_B_n.append(rang_[0])
    rang_B_E.append(rang_[1])
    rang_E_n.append(rang_[2])
    rang_E_B.append(rang_[3])
    rr_B_n.append(RR_[0])
    rr_B_E.append(RR_[1])
    rr_E_n.append(RR_[2])
    rr_E_B.append(RR_[3])


plt.title("Given bandwidth, how many workers needed")
plt.plot(dp_E_B, dp_B_n, color='green', label='DP')
plt.plot(dp_E_B, rand_B_n, color='red', label='Random')
plt.plot(dp_E_B, rang_B_n,  color='skyblue', label='RoundRobin')
plt.plot(dp_E_B, rr_B_n, color='blue', label='Local-First')
plt.legend() # 显示图例
plt.xlabel('Bandwidth')
plt.ylabel('Num of workers')
plt.show()

plt.title("Given bandwidth, how much Energy cost")
plt.plot(dp_E_B, dp_B_E, color='green', label='DP')
plt.plot(dp_E_B, rand_B_E, color='red', label='Random')
plt.plot(dp_E_B, rang_B_E,  color='skyblue', label='RoundRobin')
plt.plot(dp_E_B, rr_B_E, color='blue', label='Local-First')
plt.legend()
plt.xlabel('Bandwidth')
plt.ylabel('Energu cost')
plt.show()

plt.title("Given Energy constraint, how many workers needed")
plt.plot(dp_B_E, dp_E_n, color='green', label='DP')
plt.plot(dp_B_E, rand_E_n, color='red', label='Random')
plt.plot(dp_B_E, rang_E_n,  color='skyblue', label='RoundRobin')
plt.plot(dp_B_E, rr_E_n, color='blue', label='Local-First')
plt.legend()
plt.xlabel('Energy cost')
plt.ylabel('Num of workers')
plt.show()

plt.title("Given Energy constraint, how much bandwidth can get")
plt.plot(dp_B_E, dp_E_B, color='green', label='DP')
plt.plot(dp_B_E, rand_E_B, color='red', label='Random')
plt.plot(dp_B_E, rang_E_B,  color='skyblue', label='RoundRobin')
plt.plot(dp_B_E, rr_E_B, color='blue', label='Local-First')
plt.legend()
plt.xlabel('Energy cost')
plt.ylabel('Bandwidth')
plt.show()

