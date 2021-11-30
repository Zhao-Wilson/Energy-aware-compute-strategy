import numpy as np
from systemComfig import *
"""
This module provides a public function to randomly generate original
Energy array and Bandwidth array
"""

def generate_table():
    BW_arr = np.zeros([Nodes+1,cluster])
    Energy_arr = np.zeros([Nodes+1,cluster])

    # random.seed(0)
    # random_start_BW = [round(random.uniform(1,2),1) for i in range(cluster)]

    # build up the array format using numpy, the initial value are 50 and 0.5 respectively
    random_start_enery = [50 for i in range(cluster)]
    random_start_BW = [0.5 for i in range(cluster)]
    BW_arr[1,:] = np.array(random_start_BW)
    Energy_arr[1,:] = np.array(random_start_enery)

    # randomly adding value to the last value to fill in the original table
    for i in range(cluster):
        energy_list = np.random.randint(low=10,high=20,size=Nodes-1)
        BW_list = np.random.randint(low=1,high=10,size=Nodes-1)/10
        for j in range(2,Nodes+1):
            BW_arr[j][i] = BW_arr[j-1][i]+BW_list[j-2]
            Energy_arr[j][i] = Energy_arr[j-1][i]+energy_list[j-2]

    return BW_arr,Energy_arr


