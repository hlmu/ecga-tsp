"""
run 'python Main.py' to start.
"""
from SolutionConfig import solution_set
from entities.TSPProblem import TSPProblem

if __name__ == '__main__':
    for config in solution_set:
        TSPProblem()
        # TODO--
