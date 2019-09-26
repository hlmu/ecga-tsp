import operator
import pandas as pd
import numpy as np
import random
from entities.Population import Population

# 根据fitness作为被选中的概率，进行轮盘选择；elite_size在这里无效
def fitness_proportional(current_generation, mutation_rate, elite_size):
    rank_result = current_generation.rank_routes()

    select = []

    #将排序完的个体转换为DataFrame格式，按顺序计算出累积和cun_sum，再得出所占总适应度百分比cum_perc
    #格式样例：
    #       Index   Fitness  cum_sum  cum_perc
    # 0       1       0.5      0.5      50.0
    # 1       0       0.3      0.8      80.0
    # 2       2       0.2      1.0     100.0
    df = pd.DataFrame(np.array(rank_result), columns=["Index", "Fitness"])
    df['cum_sum'] = df.Fitness.cumsum()
    df['cum_perc'] = 100 * df.cum_sum / df.Fitness.sum()

    # 轮盘选择
    for i in range(0, len(rank_result)):
        pick = 100*random.random()
        for i in range(0, len(rank_result)):
            if pick <= df.iat[i,3]:
                select.append(rank_result[i][0])
                break

    matingpool = current_generation.mating_pool(select)

    #在整个种群上，先保留精英个体，剩下的个体两两交叉直到生成足够的数量
    children = []
    length = len(matingpool)
    pool = random.sample(matingpool, len(matingpool))

    for i in range(0, length):
        child = pool[i].crossover(pool[len(matingpool)-i-1])
        children.append(child)

    #种群中所有个体都有机会变异
    mutate_population = []

    for route in range(0, len(children)):
        # mutate_route = mutate(population[route], mutation_rate)
        mutate_route = children[route].mutate(mutation_rate)
        mutate_population.append(mutate_route)
    return Population(current_generation.selection_strategy, mutate_population)



# 精英选择
def elitism_selection(current_generation, mutation_rate, elite_size):
    rank_result = current_generation.rank_routes()

    select = []

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
        select.append(rank_result[i][0])
    for i in range(0, len(rank_result) - elite_size):
        pick = 100*random.random()
        for i in range(0, len(rank_result)):
            if pick <= df.iat[i,3]:
                select.append(rank_result[i][0])
                break

    matingpool = current_generation.mating_pool(select)

    #在整个种群上，先保留精英个体，剩下的个体两两交叉直到生成足够的数量
    children = []
    length = len(matingpool) - elite_size
    pool = random.sample(matingpool, len(matingpool))

    for i in range(0, elite_size):
        children.append(matingpool[i])

    for i in range(0, length):
        child = pool[i].crossover(pool[len(matingpool)-i-1])
        children.append(child)

    #种群中所有个体都有机会变异
    mutate_population = []

    for route in range(0, len(children)):
        # mutate_route = mutate(population[route], mutation_rate)
        mutate_route = children[route].mutate(mutation_rate)
        mutate_population.append(mutate_route)
    return Population(current_generation.selection_strategy, mutate_population)

