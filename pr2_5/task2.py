#!python3
import numpy as np


well_dept = "56 12 66 19 32 72 27 32"
well_dept = np.array(list(map(int, well_dept.split())))  # convert str to array

# step 1
average = np.average(well_dept)
print(average)

# step 2
t = (well_dept - average) ** 2.0
print(t)

# step 3
t2 = t.sum()
print(t2)

# step 4
sd_square = t2 / well_dept.shape[0]
print(sd_square)

# step 5
SD = np.sqrt(sd_square)
print(SD)

# example
print("example: ", np.std(well_dept))
