import math
import cv2
import numpy as np
import math

size = 400

res = np.linspace(-2, 2, size * 2 + 1)
ims = np.linspace(-2, 2, size * 2 + 1)


nums = np.zeros((len(res) - 1, len(ims) - 1), dtype=np.complex_)

for i in range(-size, size):
    for j in range(-size , size):
        nums[i+size, j+size] = complex(res[i+size], ims[j+size])

def function(complex_num):
    return complex_num ** 2

nums = function(nums)

phase = np.angle(nums, True)
magnitude = np.abs(nums)


H = np.interp(phase, (-180, 180), (0,  360))
S = 0.7 + (1 / 3) * (np.log(magnitude) / np.log(1.6) - np.floor(np.log(magnitude) / np.log(1.6)))   # alternatively S = 0.5 + 0.5 * (magnitude - np.floor(magnitude))

V = ((np.abs(np.sin(math.pi * nums.real)) ** 0.1) * (np.abs(np.sin(math.pi * nums.imag)) ** 0.1)) * 255 # alternatively V = np.full(phase.shape, 255, dtype="float32")


HSV = np.dstack((H, S, V)).astype("float32", copy=False)

image = cv2.cvtColor(HSV, cv2.COLOR_HSV2BGR) / 255

cv2.imshow("Complex", image)
cv2.waitKey(0)  
cv2.destroyAllWindows()  