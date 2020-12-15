import numpy as np
import copy
from ast import literal_eval
a = np.load("train_labels.npy")
with open("onlyTrainLabelsnpy.txt", 'w') as file1: 
    x = a.shape
    print(x[0])
  
    for i in range(0,x[0]):
       li_u_removed = [str(item) for item in a[i]]
       #temp = copy.deepcopy(li_u_removed)
       #print(str(temp))
       #file1.write(str(temp))
       file1.write(str(li_u_removed))
       file1.write("\n") 
