import random
from entities.Individual import Individual

#两个个体间通过交叉产生后代
def order_crossover(parent1, parent2):
    child = []
    p1 = []
    P2 = []

    #从第一个个体中随机选择一段城市，拼接第二个个体中所有不重复的城市，生成的新的个体
    geneA = int(random.random() * len(parent1.dna))
    geneB = int(random.random() * len(parent2.dna))
    start = min(geneA, geneB)
    end = max(geneA, geneB)
    for i in range(start, end):
        p1.append(parent1.dna[i])
    p2 = [item for item in parent2.dna if item not in p1]
    child = p1 + p2
    return Individual(child, parent1.mutation_operator, parent1.crossover_operator)
