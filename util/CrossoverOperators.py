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

    # 从第一个个体中随机选择一段城市，拼接第二个个体中所有不重复的城市，生成的新的个体
    geneA = int(random.random() * len(parent1.dna))
    geneB = int(random.random() * len(parent2.dna))
    start = min(geneA, geneB)
    end = max(geneA, geneB)
    dic = {}
    child = parent1.dna
    q1 = []
    q2 = []
    nums = []
    for i in range(start, end + 1):
        dic[parent2.dna[i]] = parent1.dna[i]
        q1.append(parent1.dna[i])
        q2.append(parent2.dna[i])
        nums.append(i)

    for i in range(len(q2)):
        if q2[i] not in q1:
            k = q2[i]
            dict = {}
            while k in q2:
                if k is dic[k] or k in dict.keys():
                    break
                dict[k] = dic[k]
                k = dic[k]
            flag = True
            if k in dic.keys() and k is dic[k]:
                flag = False
            if k in parent2.dna and flag is True:
                t = parent2.dna.index(k)
                child[t] = q2[i]
                nums.append(i)
    for i in range(len(child)):
        if i not in nums:
            child[i] = parent2.dna[i]
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
        if k is dic1[k]:
            break
        dic[k] = dic1[k]
        k = dic1[k]
    for i in range(len(parent1.dna)):
        if parent1.dna[i] in dic.keys():
            child.append(parent1.dna[i])
        else:
            child.append(parent2.dna[i])
    return Individual(child, parent1.mutation_operator, parent1.crossover_operator)

