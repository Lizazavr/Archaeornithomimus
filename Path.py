
import numpy as np
adj = [[1001,15,17,16,16],[15,1001,3,4,16],[17,3,1001,3,15],[16,4,3,1001,12],[16,16,15,12,1001]] #пример матр.смеж-ти
np.save("adjacency.npy",adj)

img_array = np.load('adjacency.npy')

print(img_array)
