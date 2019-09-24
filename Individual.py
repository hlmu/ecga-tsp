"""
Exercise 2 Individual and Population Representation (10 marks)

Represent a possible solution to the TSP as a permutation of the given cities and implement it in a class Individual.
Evolutionary algorithms often start with solutions that are constructed uniformly at random.
Write a method that constructs such a solution in linear time – not in O(n log n) or even O(n2), but in O(n),
where n is the number of cities.

"""
import random
import numpy as np
import matplotlib.pyplot as plt

class Individual:
    """
    This class is immutable
    """

    def __init__(self, route):
        self.dna = route.copy()

    def __len__(self):
        return len(self.dna)

    #两个个体间通过交叉产生后代
    def crossover(self, parent2):
        child = []
        p1 = []
        P2 = []

        #从第一个个体中随机选择一段城市，拼接第二个个体中所有不重复的城市，生成的新的个体
        geneA = int(random.random() * len(self.dna))
        geneB = int(random.random() * len(parent2.dna))
        start = min(geneA, geneB)
        end = max(geneA, geneB)
        for i in range(start, end):
            p1.append(self.dna[i])
        p2 = [item for item in parent2.dna if item not in p1]
        child = p1 + p2
        return Individual(child)

    #个体中的每个城市都有概率与其他城市发生顺序交换  ---> 变异
    def mutate(self, mutation_rate):
        result = Individual(self.dna)
        for swap1 in range(self.__len__()):
            if(random.random() < mutation_rate):
                swap2 = int(random.random() * self.__len__())
                city1 = result.dna[swap1]
                city2 = result.dna[swap2]
                result.dna[swap1] = city2
                result.dna[swap2] = city1
        return result

    #勾股定理求两城市间距离
    def __distance(self, city1, city2):
        x = abs(city1[0] - city2[0])
        y = abs(city1[1] - city2[1])
        distance = np.sqrt((x ** 2) + (y ** 2))
        return distance

    #适应度函数，定义为总路径的倒数
    def fitness(self):
        fitness= 0.0
        path_distance = 0
        for i in range(0, self.__len__()):
            city_from = self.dna[i]
            city_to = None
            if i + 1 < self.__len__():
                city_to = self.dna[i + 1]

            #判断是最后一个城市时，计算到第一个城市的距离
            else:
                city_to = self.dna[0]
            dist = self.__distance(city_from, city_to)
            path_distance += dist
        fitness = 1 / float(path_distance)
        return fitness

    #总路径长度
    def total_distance(self):
        path_distance = 0
        for i in range(0, self.__len__()):
            city_from = self.dna[i]
            city_to = None
            if i + 1 < self.__len__():
                city_to = self.dna[i + 1]

            #判断是最后一个城市时，计算到第一个城市的距离
            else:
                city_to = self.dna[0]
            dist = self.__distance(city_from, city_to)
            path_distance += dist
        return float(path_distance)

    #绘图
    def plotting(self, show_time):
        x = []
        y = []
        plt.cla()
        for i in range(0, self.__len__()):
            x.append(self.dna[i][0])
            y.append(self.dna[i][1])
        x.append(self.dna[0][0])
        y.append(self.dna[0][1])
        plt.plot(x, y, 'r-s', markerfacecolor = 'y')
        plt.text(0, 5500, "Total distance = %.3f" % (self.total_distance()), fontdict={'size': 20, 'color': 'blue'})
        plt.pause(show_time)

    #输出结果到文件中
    def output_city_path(self, filename):
        output = open(filename ,'w')
        output.write('----------Distance----------\n\n')
        output.write(str(self.total_distance()) + '\n\n')
        output.write('---------Circle Path--------\n\n')
        for i in self.dna:
            output.write(str(i[2]) + '\n')
        output.write(str(-1))
