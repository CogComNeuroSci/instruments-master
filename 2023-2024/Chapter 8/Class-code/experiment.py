
import numpy as np
import pandas as pd
from psychopy import data
import os

file_name = os.path.join(os.getcwd(), "some_file_name")

colors = np.array(["red", "green", "yellow", "blue"])

color = np.repeat(colors, 4)
word  = np.tile(colors, 4)
design= np.column_stack([color, word])
print(design)

design_pd = pd.DataFrame.from_records(design)
design_pd.columns = ["Color", "Word"]
print(pd.crosstab(design_pd.Color, design_pd.Word))

design_list = pd.DataFrame.to_dict(design_pd, orient = "records")

design_th = data.TrialHandler(design_list, nReps = 1, method = "sequential")

my_exp = data.ExperimentHandler(file_name)
my_exp.addLoop(design_th)

for trial in design_th:
    print(trial["Color"])
    print(trial["Word"])
    my_exp.nextEntry()




