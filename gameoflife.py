import numpy as np
import scipy.ndimage as nd

DIM = 5, 5 #Matrix dimensions
KERNEL = np.array([[1, 1, 1],
                   [1, 0, 1],
                   [1, 1, 1]], dtype=np.uint8) #"neighbour" detection

universe = np.random.randint(2, size=DIM, dtype=np.uint8) 
#"Counting" the neighbours 
neighbor_count = nd.convolve(universe, KERNEL, mode="constant")
new_state = np.empty(DIM)
np.copyto(new_state, neighbor_count, casting='same_kind')

#Applying the Game of Life rules
new_state = np.where(neighbor_count < 2, 0, neighbor_count)
new_state = np.where(neighbor_count > 3, 0, new_state)
new_state = np.where(neighbor_count == 3, 1, new_state)
new_state = np.where(neighbor_count == 2, 1, new_state)

print(universe)
print(neighbor_count) #used for debugging
print(new_state)

#TODO
#An actual interface
#Selecting the initial state of the game instead of it being randomized
