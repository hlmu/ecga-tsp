import random
from entities.Individual import Individual


# 个体中的每个城市都有概率与其他城市发生顺序交换  ---> Swap Mutation
def swap_mutation(individual, mutation_rate):
    result = Individual(individual.dna, individual.mutation_operator)
    for swap1 in range(individual.__len__()):
        if random.random() < mutation_rate:
            swap2 = int(random.random() * individual.__len__())
            city1 = result.dna[swap1]
            city2 = result.dna[swap2]
            result.dna[swap1] = city2
            result.dna[swap2] = city1
    return result


# 个体中的每个城市都有概率与其他城市发生顺序交换  ---> Insert Mutation
def insert_mutation(individual, mutation_rate):
    result = Individual(individual.dna, individual.mutation_operator)
    for insert1 in range(individual.__len__()):
        if random.random() < mutation_rate:
            insert2 = int(random.random() * individual.__len__())
            if insert1 == insert2:
                return result
            city1 = result.dna[insert1]
            city2 = result.dna[insert2]
            insert3 = min(insert1, insert2)
            insert4 = max(insert1, insert2)
            for i in range(insert3 + 1, insert4):
                result.dna[i + 1] = result.dna[i]
            if insert1 > insert2:
                result.dna[insert2 + 1] = city1
            else:
                result.dna[insert1 + 1] = city2
    return result


# 个体中的每个城市都有概率与其他城市发生顺序交换  ---> Inversion Mutation
def inversion_mutation(individual, mutation_rate):
    result = Individual(individual.dna, individual.mutation_operator)
    for swap1 in range(individual.__len__()):
        if random.random() < mutation_rate:
            swap2 = int(random.random() * individual.__len__())
            a_list = result.dna[min(swap1, swap2):max(swap1, swap2) + 1]
            a_list = a_list[::-1]
            for i in range(min(swap1, swap2), max(swap1, swap2) + 1):
                result.dna[i] = a_list[i - min(swap1, swap2)]
    return result


# 个体中的每个城市都有概率与其他城市发生顺序交换  ---> Scramble Mutation
def scramble_mutation(individual, mutation_rate):
    result = Individual(individual.dna, individual.mutation_operator)
    for swap1 in range(individual.__len__()):
        if random.random() < mutation_rate:
            swap2 = int(random.random() * individual.__len__())
            a_list = []
            for i in range(min(swap1, swap2), max(swap1, swap2) + 1):
                a_list.append(i)
            random.shuffle(a_list)
            cop = list(result.dna)
            for i in range(min(swap1, swap2), max(swap1, swap2) + 1):
                result.dna[i] = cop[a_list[i - min(swap1, swap2)]]
    return result
