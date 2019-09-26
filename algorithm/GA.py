# import some operators
import util.CrossoverOperators
import util.MutationOperators
import util.SelectionStrategy
ALG_NAME = 'GA'


class GeneticAlgorithm:
    def __init__(self):
        self.name = 'ga1'
        self.mutation_operator = util.MutationOperators.swap_mutation
        self.selection_strategy = util.SelectionStrategy.elitism_selection


class GeneticAlgorithmStar:
    def __init__(self):
        self.name = 'ga2'
        self.mutation_operator = util.MutationOperators.inversion_mutation
        # TODO new selection_strategy
        self.selection_strategy = util.SelectionStrategy.elitism_selection


class GeneticAlgorithmFinal:
    def __init__(self):
        self.name = 'ga3'
        self.mutation_operator = util.MutationOperators.scramble_mutation
        # TODO new selection_strategy
        self.selection_strategy = util.SelectionStrategy.elitism_selection
