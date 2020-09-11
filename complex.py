import math
import cv2
import numpy as np



class ComplexNum:
    def __init__(self, re, im, m=100, new=True):
        if new:
            self.re = np.tile(re, (m,1)) 
            self.im = np.rot90(np.tile(im, (m,1)))
        else:
            self.re = re
            self.im = im

    def __add__(self, other): # Add two complex nums
        return ComplexNum(self.re + other.re, self.im + other.im, new=False)

    def __mul__(self, other): # Multiply two complex nums
        re = (self.re * other.re) + (self.im * other.im * -1)
        im = self.im * other.re + self.re * other.im

        return ComplexNum(re, im, new=False)

    def __truediv__(self, other): # Divide two complex nums
        pass

    def visualRepresentation(self):
        print("{} + {}i".format(str(self.re), str(self.im)))

    def magnitude(self):
        return np.sqrt(self.re ** 2 + self.im ** 2)

    def phase(self):
        return np.arctan2(self.im, self.re) + math.pi 


def function(z):
    return z*z*z


def to_r(what):
    return (what / (2 * math.pi)) * 255

def to_g(what):
   ma = np.amax(what)
   return (what / ma) * 255

size = 400

res = np.linspace(-4, 4, size + 1)
ims = np.linspace(-4, 4, size + 1)

cnums = ComplexNum(res, ims, m=size + 1)

cnums = function(cnums)

r = to_r(cnums.phase())
g = to_g(cnums.magnitude())
b = np.full((size + 1, size + 1), 0)

np.set_printoptions(threshold=np.inf)

rgb = np.dstack((r, g, b))
rgb = rgb / 255

cv2.imshow("d", rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()

