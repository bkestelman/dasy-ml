import numpy as np

class DataSynthesizer:
    """
    Samples input X data according to a specified process.
    """
    def __init__(self):
        pass

    def sample(self, n=100, dim=2, process=np.random.normal):
        """
        Returns a sample of n data points, created by the given process.
        @param n: Number of data points to sample
        @param dim: Dimension of data
        @param process: The sampling process, for example drawing from a probability distribution.
            Must accept a size argument like numpy functions do.
        """
        return process(size=(n, dim))

class DataGenerator:
    """
    Same as DataSynthesizer but sample() returns a generator instead of all the data at once.
    """
    def __init__(self):
        pass

    def sample(self, n=100, dim=2, process=np.random.normal):
        for i in range(n):
            yield process(size=dim)

class Labeler:
    pass


