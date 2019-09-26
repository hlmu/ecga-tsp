"""
Exercise 2 Individual and Population Representation (10 marks)

A population in an evolutionary algorithms represents a set of solutions. Implement a class Population for representing
a population which is a set of individuals. Make sure that you can evaluate the quality of a solution with respect to
a given problem.
"""
import random
import operator
import pandas as pd
import numpy as np

class Population:

    def __init__(self, selection_strategy, individuals=None):
        self.selection_strategy = selection_strategy
        if individuals == None:
            self.__population = []
        else:
            self.__population = individuals.copy()

    def __len__(self):
        return len(self.__population)

    def append(self, individual):
        self.__population.append(individual)

    # 繁衍：父代种群 => 排序 -> 选择 -> 交配池 -> 交叉 -> 变异 =>子代种群
    def multiply(self, mutation_rate, elite_size=0):
        next_generation = self.selection_strategy(self, mutation_rate, elite_size)
        return next_generation

    # 生成种群内每个个体的适应度，并将它们降序排列，个体用在种群中的序号代替
    def rank_routes(self):
        fitness_results = {}
        for i in range(0,self.__len__()):
            fitness_results[i] = self.__population[i].fitness()
        return sorted(fitness_results.items(), key = operator.itemgetter(1), reverse = True)
    #将筛选完的个体的序号转化为具体的路由信息 --->生成交配池
    def mating_pool(self, select_result):
        matingpool = []
        for i in range(0, len(select_result)):
            index = select_result[i]
            matingpool.append(self.__population[index])
        return matingpool

    def min_dis(self):
        return 1 / self.rank_routes()[0][1]

    def get_best(self):
        rank = self.rank_routes()
        return self.__population[rank[0][0]]

