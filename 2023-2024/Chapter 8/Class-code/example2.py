

import numpy as np

n_block = 3
n_factor1 = 4
n_factor2 = 4
n_trial_per_block = n_factor1*n_factor2

big_matrix = np.ones((n_block*n_trial_per_block, 3)) * np.nan

for block_loop in range(n_block):
    np.random.shuffle(design_matrix) # 16 rows only!!
    rows_for_now = np.ar
    
    