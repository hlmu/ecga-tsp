"""
Configuration file
"""
POP_SIZE = 50      #每一代个体数
ELITE_SIZE = 10      #保留的精英个体数量
MUTATE_RATE = 0.002    #基因变异概率
N_GENERATIONS = 20000   #生成子代数量
CHECKPOINTS = [5000, 10000, 20000]
FILES = ['data/eil51.tsp', 'data/eil76.tsp', 'data/eil101.tsp', 'data/kroA100.tsp', 'data/kroC100.tsp',
         'data/kroD100.tsp', 'data/lin105.tsp', 'data/pcb442.tsp', 'data/pr2392.tsp', 'data/st70.tsp']
