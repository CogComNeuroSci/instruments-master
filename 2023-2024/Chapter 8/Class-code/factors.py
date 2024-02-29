

import numpy as np

n_factor1 = 4
n_factor2 = 4
n_unique  = n_factor1*n_factor2

unique = np.array(range(n_unique)) # my x's

factor1 = np.floor(unique / n_factor2) % n_factor1
factor2 = np.floor(unique / 1)         % n_factor2

congruence = (factor1 == factor2)*1

design = np.column_stack([factor1, factor2, congruence])
print(design)

