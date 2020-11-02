from resources import config
import matplotlib.pyplot as plt
import random
import math
import numpy
import numpy as np

def gauss_convert(value,m_value,sigma_value):
    gauss_value = math.exp(-(pow(m_value-value, 2))/(2 * pow(sigma_value,2)))
    return gauss_value

def choose_coordonate_random(sigma,m):
    prag = random.randint(0,100)
    prag = prag / 100
    random_coordonate = random.randint(-300,300)
    while gauss_convert(random_coordonate,m,sigma) < prag:
        random_coordonate = random.randint(-300, 300)
    return random_coordonate

def main():
    data_set = []
    graph_size = config.interval
    interval = config.interval
    zones = config.zones
    plt.xlim(graph_size[0],graph_size[1])
    plt.ylim(graph_size[0],graph_size[1])
    for i in range(0,10000):
        random_zone_key = random.choice(list(zones))
        rand_x = choose_coordonate_random(zones[random_zone_key]['interval']['sigmax'],zones[random_zone_key]['interval']['mx'])
        rand_y = choose_coordonate_random(zones[random_zone_key]['interval']['sigmay'],zones[random_zone_key]['interval']['my'])
        data_set.append([rand_x,rand_y])
        plt.scatter(rand_x,rand_y,c=zones[random_zone_key]['color'],s=1)
    #lt.show()
    np_data_set = numpy.array(data_set)
    numpy.savetxt('data_set.txt',np_data_set)
    print(np_data_set)
    print("Finish")
if __name__ == "__main__":
    main()