# Heuristic algorithms

 ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)

## Install 
```bash
# pip

$ python -m pip install -U pip
$ pip install numpy


# git

$ git clone https://github.com/sikorskayaX/heuristic-algorithms.git
```

## genetic algorithm

This code implements a genetic algorithm to find the minimum of the function f(x).

The steps that the code performs:
- Initializing the population: An initial population is created from population size individuals, each
of which is represented by an array of genes number genes. Genes are initialized with random
numbers in the range from 0 to 10.
- Fitness assessment: For each individual, the average value of its genes is calculated, and this
average value is used to calculate the value of the function f(x). Fitness of the individual
It is defined as the value of the function f(x) for this average value.
- Selection: The selection size of the best individuals (with the lowest
values of the function f(x)) is selected from the current population.
- Interbreeding: Selected individuals are interbred to create a new generation. For each
pair of parents, a crossing point is randomly selected, and
the corresponding parts of their genes are exchanged to create two offspring.
- Mutation: With some low probability of mutation rate, each gene in the population can
be randomly changed - this introduces new variations into the population.
- Repeat: Steps 2-5 are repeated for a given number of generations.
