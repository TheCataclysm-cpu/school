from resources import config
import matplotlib.pyplot as plt
import random
import math
from kmeans import kmeans_module
import numpy

def main():
    data = numpy.loadtxt('data_set.txt')
    kmeans = kmeans_module.Kmeans()
    kmeans.load_data_set(data_set=data)
    kmeans.learn()

if __name__ == "__main__":
    main()