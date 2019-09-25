"""
run 'python Main.py' to start.
"""
from SolutionConfig import solution_set
from entities.TSPProblem import TSPProblem
import os

if __name__ == '__main__':
    for config in solution_set:
        for file in config.files:
            prob = TSPProblem(file, config.alg)
            print(file + ' loaded')
            result_filename = prob.result_file_name(config.check_points[-1], config.pop_size)
            if not os.path.exists(result_filename):
                print('Working with: ' + file)
                prob.GA(config.pop_size, config.eli_size, config.mutate_rate, config.n_generations, config.check_points)
            else:
                print('Found: ' + result_filename + ', skip this instance')
