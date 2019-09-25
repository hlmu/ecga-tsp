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

    def __init__(self, individuals=None):
        if individuals == None:
            self.__population = []
        else:
            self.__population = individuals.copy()

    def __len__(self):
        return len(self.__population)

    def append(self, individual):
        self.__population.append(individual)

    #繁衍：父代种群 => 排序 -> 选择 -> 交配池 -> 交叉 -> 变异 =>子代种群
    def multiply(self, elite_size, mutation_rate):
        rank = self.__rank_routes()
        select = self.__select_routes(rank, elite_size)
        mate = self.__mating_pool(select)
        children = self.crossover_population(mate, elite_size)
        next_generation = self.__mutate_population(children, mutation_rate)
        # next_generation = children.mutate_population(mutation_rate)
        return Population(next_generation)

    #生成种群内每个个体的适应度，并将它们降序排列，个体用在种群中的序号代替
    def __rank_routes(self):
        fitness_results = {}
        for i in range(0,self.__len__()):
            fitness_results[i] = self.__population[i].fitness()
        return sorted(fitness_results.items(), key = operator.itemgetter(1), reverse = True)

    #筛选个体
    def __select_routes(self, rank_result, elite_size):
        select_result = []

        #将排序完的个体转换为DataFrame格式，按顺序计算出累积和cun_sum，再得出所占总适应度百分比cum_perc
        #格式样例：
        #       Index   Fitness  cum_sum  cum_perc
        # 0       1       0.5      0.5      50.0
        # 1       0       0.3      0.8      80.0
        # 2       2       0.2      1.0     100.0
        df = pd.DataFrame(np.array(rank_result), columns=["Index", "Fitness"])
        df['cum_sum'] = df.Fitness.cumsum()
        df['cum_perc'] = 100 * df.cum_sum / df.Fitness.sum()

        #先保留精英个体，将剩下个体进行轮盘赌选择
        for i in range(0, elite_size):
            select_result.append(rank_result[i][0])
        for i in range(0, len(rank_result) - elite_size):
            pick = 100*random.random()
            for i in range(0, len(rank_result)):
                if pick <= df.iat[i,3]:
                    select_result.append(rank_result[i][0])
                    break
        return select_result

    #将筛选完的个体的序号转化为具体的路由信息 --->生成交配池
    def __mating_pool(self, select_result):
        matingpool = []
        for i in range(0, len(select_result)):
            index = select_result[i]
            matingpool.append(self.__population[index])
        return matingpool


    #在整个种群上，先保留精英个体，剩下的个体两两交叉直到生成足够的数量
    def crossover_population(self, matingpool, elite_size):
        children = []
        length = len(matingpool) - elite_size
        pool = random.sample(matingpool, len(matingpool))

        for i in range(0, elite_size):
            children.append(matingpool[i])

        for i in range(0, length):
            child = pool[i].crossover(pool[len(matingpool)-i-1])
            children.append(child)
        return children

    def min_dis(self):
        return 1 / self.__rank_routes()[0][1]

    def get_best(self):
        rank = self.__rank_routes()
        return self.__population[rank[0][0]]

    #种群中所有个体都有机会变异
    def __mutate_population(self, population, mutation_rate):
        mutate_population = []

        for route in range(0, len(population)):
            # mutate_route = mutate(population[route], mutation_rate)
            mutate_route = population[route].mutate(mutation_rate)
            mutate_population.append(mutate_route)
        return mutate_population

