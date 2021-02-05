import math
import cv2
import numpy as np
import math

# Setup
size = 800
x_range = 3
y_range = x_range
threshold = 0.01 # Black line visibility

res = np.linspace(-(x_range / 2), x_range / 2, size * 2 + 1)
ims = np.linspace(-(y_range / 2), y_range / 2, size * 2 + 1)

nums = np.zeros((len(res) - 1, len(ims) - 1), dtype=np.complex_)

for i in range(-size, size):
    for j in range(-size , size):
        nums[i+size, j+size] = complex(ims[i+size], res[j+size])

def g(z):
    return (z - 1) / (z ** 13 + z + 1)

def function(z):
    return z ** (1 + 10j) * np.cos(g(z))


nums = function(nums)

phase = np.angle(nums, True)
magnitude = np.abs(nums)


H = np.interp(phase, (-180, 180), (0,  360))
S = 0.7 + (1 / 3) * (np.log(magnitude) / np.log(1.6) - np.floor(np.log(magnitude) / np.log(1.6)))   # alternatively S = 0.5 + 0.5 * (magnitude - np.floor(magnitude))
V = ((np.abs(np.sin(math.pi * nums.real)) ** threshold) * (np.abs(np.sin(math.pi * nums.imag)) ** threshold)) * 255 # alternatively V = np.full(phase.shape, 255, dtype="float32")


HSV = np.dstack((H, S, V)).astype("float32", copy=False)

image = np.rot90(cv2.cvtColor(HSV, cv2.COLOR_HSV2BGR) / 255, 3)

# cv2.imwrite("complex.png", image * 255)

cv2.imshow("Complex", image)
cv2.waitKey(0)  
cv2.destroyAllWindows()  