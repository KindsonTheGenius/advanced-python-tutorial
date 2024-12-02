from multiprocessing import Process
from multiprocessing.shared_memory import SharedMemory
import numpy as np
def worker(shared_name, shape):
    
    # Attach to existing shared memory
    existing_shm = SharedMemory(name=shared_name)

    # Create a Numpy array backed by shared memory
    shared_array = np.ndarray(shape, dtype=np.int64, buffer=existing_shm.buf)

    # Modify the shared array
    shared_array[0] += 100