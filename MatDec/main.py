from scipy import misc
import matplotlib.pyplot as plt
img = misc.face()
print(img.shape)
print(img.ndim)
print(img[:,:,0])


