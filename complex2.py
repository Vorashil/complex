import math
import cv2
import numpy as np
import math

size = 400

res = np.linspace(-8, 8, size * 2 + 1)
ims = np.linspace(-8, 8, size * 2 + 1) * 1j

nums = np.zeros((len(res) - 1, len(ims) - 1), dtype=np.complex_)

for i in range(-size, size):
    for j in range(-size , size):
        nums[i+size, j+size] = complex(j, i)

def function(complex_num):
    return complex_num ** 2


nums = function(nums)

phase = np.angle(nums, True)
magnitude = np.abs(nums)


H = np.interp(phase, (-180, 180), (0,  360))
L = np.interp(magnitude, (0, np.amax(magnitude)), (0,  1))
S = np.full(phase.shape, 255, dtype="float32")

for x, y in np.ndindex(L.shape):
    L[x][y] = 0.5 + 0.5 * (L[x][y] - math.floor(L[x][y]))


HLS = np.dstack((H, S, L)).astype("float32", copy=False)
np.set_printoptions(threshold=np.inf)

image = cv2.cvtColor(HLS, cv2.COLOR_HLS2BGR) / 255

cv2.imshow("Complex", image)
cv2.waitKey(0)  
cv2.destroyAllWindows()  