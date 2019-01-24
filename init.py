import numpy as np

class Network(object):
    
    def __init__(self, sizes):
        self.layer_count = len(sizes);
        self.layers = sizes;
        self.biases = [np.random.randn(y, 1) for y in sizes[1:]]
        self.weights = [np.random.randn(x, y) for x, y in zip(sizes[:-1], sizes[1:])]