# import some operators
import util.CrossoverOperators
import util.MutationOperators
import util.SelectionStrategy
ALG_NAME = 'GA'


class GeneticAlgorithm:
    def __init__(self):
        self.name = 'ga1'
        self.mutation_operator = util.MutationOperators.swap_mutation


class GeneticAlgorithmStar:
    def __init__(self):
        self.name = 'ga2'
        self.mutation_operator = util.MutationOperators.inversion_mutation

class GeneticAlgorithmFinal:
    def __init__(self):
        self.name = 'ga3'
        self.mutation_operator = util.MutationOperators.scramble_mutation
