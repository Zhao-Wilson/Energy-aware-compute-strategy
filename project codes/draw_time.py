import matplotlib.pyplot as plt
import numpy as np

k_6 = [0.000114918,0.00013113,0.000149965,0.000169992,0.000205755,0.000204086,0.000221968,0.000257015,0.000304937,0.000292063,
       0.000302076,0.000339985,0.000369072,0.000412941,0.000430822,0.000458002,0.000488997,0.000520945,0.000580072,0.000591755,0.000624895]

k_5 = [0.004928112,0.007091045,0.008605957,0.010834932,0.014414787,0.017094851,0.020362854,0.024487972,0.030019999,0.035350084,
       0.036017895,0.045539141,0.05663991,0.06281209,0.072049141,0.079575062,0.087878942,0.100127935,0.114283085,0.122385025,0.138761044]

k_4 = [0.087253094,0.126269102,0.176642179,0.232936859,0.280097008,0.404313803,0.500750065,0.609941959,0.760712862,0.913477898,
       1.052338123,1.252687693,1.60037899,1.859317064,1.951334,2.291534901,2.836351156,3.013049841,3.650532961,4.073465109,4.529249907]

k_3 = [0.516419172,0.646169901,0.964924097,1.174201012,1.331890821,1.955546141,2.24103713,2.70542407,3.198145151,3.887562037,
       4.102843046,4.98266983,6.298829079,6.719922066,7.293964148,8.909402847,9.690003157,11.40235591,12.5094769,14.09337592,14.89216471]

k_2 = [1.100208044,1.390288115,1.988276005,2.426803827,2.849555969,4.028712988,4.475614071,5.347027063,6.309726954,7.5785532,
       8.040798903,9.975610733,11.95900702,12.83031702,13.68762493,16.84895301,18.80254984,21.33556724,21.90687895,24.70759082,26.37702084]

k_1 = [1.860599041,2.53719306,3.275767088,4.096364975,4.831798077,6.839805841,7.190618753,8.712460041,10.6241219,12.64528704,
       12.31071997,15.35254097,18.90699792,19.92475605,20.99453497,26.35791016,29.10081291,32.44328809,34.77020288,39.55430722,43.19068098]

search_time = [0.001483917,0.001605988,0.002441168,0.001988888,0.002261162,0.002461162,0.002599239,0.002788305,0.003075123,
               0.002861023,0.003049135,0.003103971,0.003464937,0.003622055,0.003537178,0.003874063,0.004317999,0.004408121,
               0.004236937,0.0043962,0.004496]

Nodes = [10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]

k6 = np.array(k_6)
k5 = np.array(k_5)
k4 = np.array(k_4)
k3 = np.array(k_3)
k2 = np.array(k_2)
k1 = np.array(k_1)
all = np.vstack((k6,k5,k4,k3,k2,k1))

# for i in range(len(k1)):
#     all[:,i] = all[:,i]

# print(all)

plt.title("Reuse last phase Table")
plt.plot(Nodes, all[5,:]-all[4,:], color='orange', label='k_1')
plt.plot(Nodes, all[4,:]-all[3,:], color='blue', label='k_2')
plt.plot(Nodes, all[3,:]-all[2,:],  color='skyblue', label='k_3')
plt.plot(Nodes, all[2,:]-all[1,:], color='red', label='k_4')
plt.plot(Nodes, all[1,:]-all[0,:], color='green', label='k_5')
plt.plot(Nodes, all[0,:], color='purple', label='k_6')
plt.plot(Nodes, search_time, color='violet', label='search_time')
plt.legend() # 显示图例
plt.xlabel('Num of workers')
plt.ylabel('Time (s)')
plt.show()


# N_10 = [0.000114918,0.004928112,0.087253094,0.516419172,1.100208044,1.860599041]
#
# N_15 = [0.000204086,0.017094851,0.404313803,1.955546141,4.028712988,6.839805841]
#
# N_20 = [0.000302076,0.036017895,1.052338123,4.102843046,8.040798903,12.31071997]
#
# N_25 = [0.000458002,0.079575062,2.291534901,8.909402847,16.84895301,26.35791016]
#
# N_30 = [0.000624895,0.138761044,4.529249907,14.89216471,26.37702084,43.19068098]
#
# x_ = [1,2,3,4,5,6]
#
# plt.title("For every certain K, how much time for given num of workers")
# plt.plot(x_, N_30, color='blue', label='worker_30')
# plt.plot(x_, N_25,  color='skyblue', label='worker_25')
# plt.plot(x_, N_20, color='red', label='worker_20')
# plt.plot(x_, N_15, color='green', label='worker_15')
# plt.plot(x_, N_10, color='purple', label='worker_10')
# plt.legend() # 显示图例
# plt.xlabel('K phase')
# plt.ylabel('Time (s)')
# plt.show()