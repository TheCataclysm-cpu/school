from resources import config
import matplotlib.pyplot as plt
import random
import math

def gauss_convert(value,m_value,sigma_value):
    gauss_value = math.exp(-(pow(m_value-value, 2))/(2 * pow(sigma_value)))
    return gauss_value

def main():
    graph_size = config.interval
    interval = config.interval
    zones = config.zones
    plt.xlim(graph_size[0],graph_size[1])
    plt.ylim(graph_size[0],graph_size[1])
    plt.show()
    for i in range(0,10000):
        random_zone_key = random.choice(list(zones))
        random_x = random.randint(interval[0],interval[1])


if __name__ == "__main__":
    main()