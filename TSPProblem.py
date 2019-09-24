"""
Exercise 1 Problem Representation and TSPlib (5 points)
Harbin Institute of Technology – University of Adelaide September 2019

Write a class TSPProblem which represents the TSP problem. Your class should enable the construction of TSP problems
from the files of the symmetric traveling salesperson problem of the TSPlib.
"""

from Parser import Parser
import random
from Parser import Parser
from config import *
from Individual import Individual
from Population import Population
import os
City = complex # create alias for the complex

class TSPProblem:

    def __init__(self, filename):
        """
        build up city coordinates.
        :param filename: tsp file name
        """
        self.filename = filename
        self.citylist = []
        __raw_data = Parser(filename).data
        # self.citylist = [<city_index>] = <coordinate of city>
        for item in __raw_data['map']:
            self.citylist.append((item[1],  item[2]))

    #创建一个城市的随机访问路径 --->个体
    def create_routes(self, citylist):
        # route = random.sample(citylist, len(citylist))
        route = Individual(random.sample(citylist, len(citylist)))
        return route

    #创建足够多的个体 --->初始种群
    def initial_population(self, population_size, citylist):
        population = Population()
        for i in range(0, population_size):
            population.append(self.create_routes(citylist))
        return population

    def read_city_file(self, citylist, filename):
        __raw_data = Parser(filename).data
        map_size = len(__raw_data['map'])
        # cities_table[<city_index>] = <coordinate of city>
        for item in __raw_data['map']:
            citylist.append((item[1],  item[2]))


    #繁衍
    def multiply_of_each_generation(self, generation, population, elite_size, mutation_rate):
        # population = multiply(population, elite_size, mutation_rate)
        population = population.multiply(elite_size, mutation_rate)
        min_dis = population.min_dis()
        print('Gen:', generation,'|| best fit:', min_dis)
        #注释下一行可以只绘制最终结果的图像
        # plotting(population[0], best, 0.01)
        return population

    #繁衍最后一代
    def multiply_of_last_generation(self, generation, population, elite_size, mutation_rate):
        # population = multiply(population, elite_size, mutation_rate)
        population = population.multiply(elite_size, mutation_rate)
        min_dis = population.min_dis()
        print('Gen:', generation,'|| best fit:', min_dis)
        #最后一张绘图停留两秒后消失
        best = population.get_best()
        best.plotting(2)
        print("Final Distance = %.3f" % min_dis)
        type = os.path.splitext(os.path.basename(self.filename))[0]
        best.output_city_path(type)

    def GA(self, pop_size, elite_size, mutation_rate, generation):
        population = self.initial_population(pop_size, self.citylist)
        for gen in range(1, generation):
            population = self.multiply_of_each_generation(gen, population, elite_size, mutation_rate)
        self.multiply_of_last_generation(generation, population, elite_size, mutation_rate)

if __name__ == '__main__':
    prob = TSPProblem('data/eil51.tsp')
    prob.GA(POP_SIZE, ELITE_SIZE, MUTATE_RATE, N_GENERATIONS)
