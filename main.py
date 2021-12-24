import numpy as np
import matplotlib.pyplot as plt
from synthesizers.gaussian import GaussianSynth
from labelers.centroids import CentroidsLabeler

def main():
    dim = 2

    synth = GaussianSynth()
    data = synth.sample(n=100, dim=dim)
    #plt.scatter(data.T[0], data.T[1])
    #plt.show()

    labeler = CentroidsLabeler(classes=2, dim=dim)
    labels = labeler.assign(data)
    plt.scatter(data.T[0], data.T[1], c=labels)
    plt.show()

if __name__ == '__main__':
    main()

