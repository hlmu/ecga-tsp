"""
Configuration file
you can add more than one config to test examples.
"""
from algorihm.GA import GeneticAlgorithm
from algorihm.GA import GeneticAlgorithmStar
from algorihm.GA import GeneticAlgorithmFinal

DEFAULT_POP_SIZE = 50      # 每一代个体数
DEFAULT_ELITE_SIZE = 10      # 保留的精英个体数量
DEFAULT_MUTATE_RATE = 0.002    # 基因变异概率
DEFAULT_N_GENERATIONS = 20000   # 生成子代数量
DEFAULT_CHECKPOINTS = [5000, 10000, 20000]
DEFAULT_FILES = ['data/eil51.tsp', 'data/eil76.tsp', 'data/eil101.tsp', 'data/kroA100.tsp', 'data/kroC100.tsp',
                 'data/kroD100.tsp', 'data/lin105.tsp', 'data/pcb442.tsp', 'data/pr2392.tsp', 'data/st70.tsp']
DEFAULT_END = 20000
DEFAULT_ALG = GeneticAlgorithm()


class Solution:
    def __init__(self, pop_size=DEFAULT_POP_SIZE, eli_size=DEFAULT_ELITE_SIZE,
                 mutate_rate=DEFAULT_MUTATE_RATE, n_generations=DEFAULT_N_GENERATIONS,
                 check_points=DEFAULT_CHECKPOINTS, files=DEFAULT_FILES, end=DEFAULT_END,
                 alg=DEFAULT_ALG
                 ):
        self.pop_size = pop_size
        self.eli_size = eli_size
        self.mutate_rate = mutate_rate
        self.n_generations = n_generations
        self.check_points = check_points
        self.files = files
        self.end = end
        self.alg = alg
        # 在此添加更多的参数等


solution_set = list()

f_list = ['data/kroA100.tsp', 'data/kroC100.tsp', 'data/kroD100.tsp']
solution_set.append(Solution(files=f_list, pop_size=10, alg=GeneticAlgorithm()))
solution_set.append(Solution(files=f_list, pop_size=20, alg=GeneticAlgorithm()))
solution_set.append(Solution(files=f_list, pop_size=50, alg=GeneticAlgorithm()))
solution_set.append(Solution(files=f_list, pop_size=100, alg=GeneticAlgorithm()))

solution_set.append(Solution(files=f_list, pop_size=10, alg=GeneticAlgorithmStar()))
solution_set.append(Solution(files=f_list, pop_size=20, alg=GeneticAlgorithmStar()))
solution_set.append(Solution(files=f_list, pop_size=50, alg=GeneticAlgorithmStar()))
solution_set.append(Solution(files=f_list, pop_size=100, alg=GeneticAlgorithmStar()))

solution_set.append(Solution(files=f_list, pop_size=10, alg=GeneticAlgorithmFinal()))
solution_set.append(Solution(files=f_list, pop_size=20, alg=GeneticAlgorithmFinal()))
solution_set.append(Solution(files=f_list, pop_size=50, alg=GeneticAlgorithmFinal()))
solution_set.append(Solution(files=f_list, pop_size=100, alg=GeneticAlgorithmFinal()))
