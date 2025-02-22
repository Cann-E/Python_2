import numpy as np

height=[1,2,3,4]
weight=[5,6,7,8]

np_height=np.array(height)
np_weight=np.array(weight)

bmi=np_height/np_weight **2
print(bmi)
print(bmi[3])
print(bmi>0.05)
print(bmi[bmi>0.05])