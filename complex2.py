import math
import cv2
import numpy as np

size = 10

res = np.linspace(-size, size, size * 2 + 1)
ims = np.linspace(-size, size, size * 2 + 1) * 1j

nums = np.zeros((len(res) - 1, len(ims) - 1), dtype=np.complex_)

for i in range(-size, size):
    for j in range(-size , size):
        nums[i+size, j+size] = complex(i, j)   #<-- to maintain the expected shape

def function(complex_num):
    return complex_num-2j

print(nums[1])
print(function(nums)[1])
