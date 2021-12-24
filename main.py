import numpy as np
import matplotlib.pyplot as plt
from synthesizers.gaussian import GaussianSynth
from labelers.centroids import CentroidsLabeler

def main():
    dim = 2
    plt.gca().set_aspect('equal', adjustable='box')

    synth = GaussianSynth()
    data = synth.sample(n=100, dim=dim)
    #plt.scatter(data.T[0], data.T[1])
    #plt.show()

    labeler = CentroidsLabeler(classes=2, dim=dim)
    labels = labeler.assign(data)
    plt.scatter(data.T[0], data.T[1], c=labels)
    plt.scatter(labeler.centroids.T[0], labeler.centroids.T[1], c='r')
    plt.plot(labeler.centroids.T[0], labeler.centroids.T[1], '--')
    plot_bisectors(labeler.centroids[0], labeler.centroids[1])
    plt.title('Gaussian Data with Centroid Labeling')
    plt.show()

def plot_bisectors(a, b):
    midpoint = (a + b) / 2
    slope = - (b[0] - a[0]) / (b[1] - a[1])
    #plt.plot([midpoint[0], midpoint[0] + 1], [midpoint[1], midpoint[1] + slope], '-')
    plt.axline((midpoint[0], midpoint[1]), slope=slope, linestyle='--')

if __name__ == '__main__':
    main()

