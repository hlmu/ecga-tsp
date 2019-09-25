"""
Exercise 1 Problem Representation and TSPlib (5 points)
Harbin Institute of Technology – University of Adelaide September 2019

Write a class TSPProblem which represents the TSP problem. Your class should enable the construction of TSP problems
from the files of the symmetric traveling salesperson problem of the TSPlib.
"""

import random
from util.Parser import Parser
from config import *
from entities.Individual import Individual
from entities.Population import Population
import os
City = complex # create alias for the complex

class TSPProblem:

    def __init__(self, filename, alg):
        """
        build up city coordinates.
        :param filename: tsp file name
        """
        self.filename = filename
        self.citylist = []
        self.alg = alg
        __raw_data = Parser(filename).data
        # self.citylist  = <x_coordinate, y_coordinate, city_index>
        for item in __raw_data['map']:
            self.citylist.append((item[1],  item[2], item[0]))

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

    #得到输出结果文件名
    def result_file_name(self, gen):
        type = os.path.splitext(os.path.basename(self.filename))[0]
        result_file_name = 'results/' + type + '-' + self.alg + '-' + str(gen) + '.txt'
        return result_file_name

    #繁衍
    def multiply_of_each_generation(self, generation, population, elite_size, mutation_rate, checkpoints=None):
        # population = multiply(population, elite_size, mutation_rate)
        population = population.multiply(elite_size, mutation_rate)
        min_dis = population.min_dis()
        print('Gen:', generation,'|| best fit:', min_dis)
        #注释下一行可以只绘制最终结果的图像
        # plotting(population[0], best, 0.01)

        if checkpoints and generation in checkpoints:
            #最后一张绘图停留两秒后消失
            best = population.get_best()
            best.plotting(2)
            print("Gen " + str(generation) + " Distance = %.3f" % min_dis)
            filename = self.result_file_name(generation)
            best.output_city_path(filename)
        return population

    def GA(self, pop_size, elite_size, mutation_rate, generation, checkpoints=None):
        population = self.initial_population(pop_size, self.citylist)
        for gen in range(1, generation+1):
            population = self.multiply_of_each_generation(gen, population, elite_size, mutation_rate, checkpoints)
        # self.multiply_of_last_generation(generation, population, elite_size, mutation_rate)

# 此处可以用于编辑算法的时候测试， 批量测试配置config后运行Main.py
if __name__ == '__main__':
    for file in FILES:
        prob = TSPProblem(file, 'alg1')
        print(file + ' loaded')
        result_filename = prob.result_file_name(CHECKPOINTS[-1])
        if not os.path.exists(result_filename):
            print('Working with: ' + file)
            prob.GA(POP_SIZE, ELITE_SIZE, MUTATE_RATE, N_GENERATIONS, CHECKPOINTS)
        else:
            print('Found: ' + result_filename + ', skip this instance')
