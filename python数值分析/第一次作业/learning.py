import numpy as np
int_arr =np.array([1,2,3])
print(int_arr)
print(int_arr.dtype)
float_arr=np.array([1.1,2.2,3.3])
print(float_arr)
print(float_arr.dtype)
bool_arr=int_arr>=2
print (bool_arr)
print (bool_arr.dtype)
print(np.where(bool_arr))