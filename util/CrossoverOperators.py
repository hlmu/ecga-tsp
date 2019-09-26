import random
from entities.Individual import Individual


# 两个个体间通过交叉产生后代  ---> Order Crossover
def order_crossover(parent1, parent2):
    child = []
    p1 = []
    p2 = []

    # 从第一个个体中随机选择一段城市，拼接第二个个体中所有不重复的城市，生成的新的个体
    geneA = int(random.random() * len(parent1.dna))
    geneB = int(random.random() * len(parent2.dna))
    start = min(geneA, geneB)
    end = max(geneA, geneB)
    for i in range(start, end + 1):
        p1.append(parent1.dna[i])
    for i in range(end + 1, end + len(parent1.dna) + 1):
        cou = i
        if cou >= len(parent1.dna):
            cou -= len(parent1.dna)
        if parent2.dna[cou] not in p1:
            p2.append(parent2.dna[cou])
    child = p2[len(parent2.dna) - end:] + p1 + p2[:len(parent2.dna) - end]
    return Individual(child, parent1.mutation_operator, parent1.crossover_operator)


# 两个个体间通过交叉产生后代  ---> PBX Crossover
def PBX_crossover(parent1, parent2):
    child = []
    p1 = []
    p2 = []

    # 从第一个个体中随机选择一段城市，拼接第二个个体中所有不重复的城市，生成的新的个体
    geneA = int(random.random() * len(parent1.dna))
    geneB = int(random.random() * len(parent2.dna))
    start = min(geneA, geneB)
    end = max(geneA, geneB)
    dic = {}
    for i in range(start, end + 1):
        p1.append(parent2.dna[i])
        dic[parent2.dna[i]] = parent1.dna[i]

    for i in range(end + 1, start + len(parent1.dna) + 1):
        cou = i
        if cou >= len(parent1.dna):
            cou -= len(parent1.dna)
        if parent1.dna[cou] in p1:
            k = dic[parent1.dna[cou]]
            while k in p1:
                k = dic[k]
            p2.append(k)
    child = p2[len(parent2.dna) - end:] + p1 + p2[:len(parent2.dna) - end]
    return Individual(child, parent1.mutation_operator, parent1.crossover_operator)


# 两个个体间通过交叉产生后代  ---> Cycle Crossover
def cycle_crossover(parent1, parent2):
    child = []
    p1 = []
    p2 = []

    # 从第一个个体中随机选择一段城市，拼接第二个个体中所有不重复的城市，生成的新的个体
    geneA = int(random.random() * len(parent1.dna))
    dic = {}
    dic1 = {}
    for i in range(len(parent1.dna)):
        dic1[parent1.dna[i]] = parent2.dna[i]
    dic[parent1.dna[geneA]] = parent2.dna[geneA]
    k = parent2.dna[geneA]
    while k != parent1.dna[geneA]:
        dic[k] = dic1[k]
        k = dic1[k]
    for i in range(len(parent1.dna)):
        if parent1.dna[i] in dic.keys():
            child += parent1.dna[i]
        else:
            child += parent2.dna[i]
    return Individual(child, parent1.mutation_operator, parent1.crossover_operator)
