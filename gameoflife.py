import numpy as np
import scipy.ndimage as nd

DIM = 5, 5
KERNEL = np.array([[0, 1, 0],
                   [1, 0, 1],
                   [0, 1, 0]], dtype=np.uint8)

universe = np.random.randint(2, size=DIM, dtype=np.uint8)
neighbor_count = nd.convolve(universe, KERNEL, mode="constant")
new_state = np.empty(DIM)
np.copyto(new_state, neighbor_count, casting='same_kind')

new_state = np.where(neighbor_count < 2, 0, neighbor_count)
new_state = np.where(neighbor_count > 3, 0, new_state)
new_state = np.where(neighbor_count == 3, 1, new_state)
new_state = np.where(neighbor_count == 2, 1, new_state)

print(universe)
print(neighbor_count)
print(new_state)