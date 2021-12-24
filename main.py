import numpy as np
import matplotlib.pyplot as plt
from core import DataSynthesizer, DataGenerator, Labeler

def main():
    synth = DataSynthesizer()
    data = synth.sample(n=100, dim=2)
    plt.scatter(data.T[0], data.T[1])
    plt.show()

if __name__ == '__main__':
    main()

