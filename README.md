# ecga-tsp
Evolutionary Computation Group Assignment: The Traveling Salesperson Problem - Implementation

### TSPProblem.py
Write a class TSPProblem which represents the TSP problem. Your class should enable the construction 
of TSP problems from the files of the symmetric traveling salesperson problem of the TSPlib, which is available online:

### Individual.py
Represent a possible solution to the TSP as a permutation of the given cities and implement it in 
a class Individual. Evolutionary algorithms often start with solutions that are constructed uniformly at random. 
Write a method that constructs such a solution in linear time – not in O(n log n) or even O(n2), but in O(n), where n 
is the number of cities.

### Population.py
A population in an evolutionary algorithms represents a set of solutions. Implement a class Population 
for representing a population which is a set of individuals. Make sure that you can evaluate the quality of a solution 
with respect to a given problem.