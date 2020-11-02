import random
import numpy
from resources import config
import matplotlib
matplotlib.use("TkAgg")
import pylab

class Kmeans:

    def __init__(self):
        self.__data_set = None
        self.__number_of_centroids = config.max_number_of_centroids
        self.__centroids_dict = {}
        self.__interval = config.interval

    def load_data_set(self,data_set):
        self.__data_set = data_set

    def __calculate_distance(self,coordonates,entry_coordonates):
        np_coordonates = numpy.array(coordonates)
        np_entry_coordonates = numpy.array(entry_coordonates)
        distance = numpy.linalg.norm(np_coordonates - np_entry_coordonates)
        return distance

    def __compute_clusters(self,centroids_coordonates):
        clusters = {}
        distances = {}
        for centroid in centroids_coordonates:
            clusters[centroid] = []
        for entry in self.__data_set:
            for centroid,coordonates in centroids_coordonates.items():
                distances[centroid] = self.__calculate_distance(coordonates,entry)
            clusters[min(distances,key=distances.get)].append(entry)
        return clusters

    def __calculate_means(self,clusters):
        means = {}
        for centroid in clusters:
            means[centroid] = numpy.array(clusters[centroid]).mean(axis=0)
        return means

    def learn(self):
        clusters = {}
        E_array = []
        nr_of_centroids_array = []
        for centroid_numbers in range(3,self.__number_of_centroids):
            centroids_coordonates = self.__get_random_centroid_coordonates(centroid_numbers)
            E = 0
            epoch = 1;
            while True:
                clusters = self.__compute_clusters(centroids_coordonates)
                means_of_clusters = self.__calculate_means(clusters)
                for centroid in means_of_clusters:
                    centroids_coordonates[centroid] = means_of_clusters[centroid]
                new_E = self.__calculate_convergence(clusters,centroids_coordonates)
                if E == new_E:
                    nr_of_centroids_array.append(centroid_numbers)
                    E_array.append(E)
                    break
                else:
                    E = new_E
                    title = "Finish epoch:" + str(epoch) + "number of centroids:" + str(centroid_numbers)
                    self.__print_epoch(clusters, centroids_coordonates,title)
                epoch = epoch + 1
        #self.__plot_ellbow(nr_of_centroids_array,E_array)





    def __get_random_centroid_coordonates(self, centroid_numbers):
        centroids_coordonates = {}
        interval_max = self.__interval[1]
        interval_min = self.__interval[0]
        for centroid in range(1,centroid_numbers+1):
            centroids_coordonates[str(centroid)] = [random.randint(interval_min,interval_max),random.randint(interval_min,interval_max)]
        return centroids_coordonates

    def __calculate_convergence(self, clusters, centroids_coordonates):
        E = 0
        for centroid in clusters:
            cluster_sum = 0
            for point in clusters[centroid]:
                cluster_sum = cluster_sum + self.__calculate_distance(centroids_coordonates[centroid],point)
            E = E + cluster_sum
        return E

    def __print_epoch(self, clusters, centroids_coordonates,title):
        pylab.figure()
        colors = config.colors
        graph_size = config.interval
        pylab.xlim(graph_size[0], graph_size[1])
        pylab.ylim(graph_size[0], graph_size[1])
        for centroid in clusters:
            pylab.scatter(centroids_coordonates[centroid][0],centroids_coordonates[centroid][1],c=colors[centroid],s=15)
            for point in clusters[centroid]:
                pylab.scatter(point[0],point[1],c=colors[centroid],s=1)
        pylab.xlabel('X')
        pylab.ylabel('Y')
        pylab.title(title)
        pylab.show()

    def __plot_ellbow(self,nr_of_centroids_array,E_array):
        pylab.figure(figsize=(16, 8))
        pylab.plot(nr_of_centroids_array, E_array, 'bx-')
        pylab.xlabel('k')
        pylab.ylabel('Distortion')
        pylab.title('The Elbow Method showing the optimal k')
        pylab.show()