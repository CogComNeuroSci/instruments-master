''' CE 11.4: Unbalanced designs
A different approach for unbalanced designs. The advantage of this one is that it's easier to
the number of observations per condition'''
from psychopy import data
import pandas, random

directions = ["left", "right"]
n_per_cond = [8,8,8,8,2,2,2,2]
factors = ["arrow", "word_text", "word_location"]
con1 = ["left","left","left"]
con2 = ["left","left","right"]
con3 = ["left","right","left"]
con4 = ["left","right","right"]
con5 = ["right","left","left"]
con6 = ["right","left","right"]
con7 = ["right","right","left"]
con8 = ["right","right","right"]
con = pandas.DataFrame([con1, con2, con3, con4, con5, con6, con7, con8], columns = factors)

pd = pandas.DataFrame(columns = factors)
for loop in range(len(n_per_cond)):
    pd = pd.append([con.iloc[loop,:]]*n_per_cond[loop], ignore_index = True)

index = list(pd.index)
random.shuffle(index)
pd = pd.loc[index]
pd["congruent"] = pd["arrow"]==pd["word_text"]
pd["correct_response"] = pd["word_text"]
pd["correct_response"] = pd["correct_response"].replace(["left","right"],["f","j"])
print(pandas.crosstab([pd.arrow,pd.word_text],pd.word_location))
#print(pd)

# and back to Dict
trial_list_extended = pandas.DataFrame.to_dict(pd, orient = "records")
print(len(trial_list_extended))