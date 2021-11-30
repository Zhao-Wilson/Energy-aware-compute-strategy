from generateNodes import *
from dp import *
from search_DP import *

BW_arr,Energy_arr = generate_table()
dp_table = build_dp_table(3000,Energy_arr,BW_arr)
search_best_choice(20000,dp_table,Energy_arr)
