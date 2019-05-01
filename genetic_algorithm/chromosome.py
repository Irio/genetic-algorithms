import random
import string

import numpy as np

# IDEAL_CHROMOSOME = "IRIOMUSSKOPF"
IDEAL_CHROMOSOME = string.ascii_uppercase
LENGTH = len(IDEAL_CHROMOSOME)
POSSIBLE_GENES = string.ascii_letters


class Chromosome:
    def __init__(self, genes, mutation_probability=1 / LENGTH):
        self.genes = genes
        self.mutation_probability = mutation_probability
        self._fitness = None

    def __repr__(self):
        return f"Chromosome({''.join(self.genes)})"

    def __eq__(self, other):
        return self.genes == other.genes

    def __lt__(self, other):
        return self.fitness() < other.fitness()

    def random():
        possible_genes = np.array(list(POSSIBLE_GENES))
        genes = np.random.choice(possible_genes, LENGTH, replace=True)
        return Chromosome(genes)

    def fitness(self):
        if self._fitness is None:
            value = 0
            for gene, ideal in zip(self.genes, IDEAL_CHROMOSOME):
                if gene == ideal:
                    value += 1
            self._fitness = value
        return self._fitness

    def mutated(self):
        mutations = np.random.choice(list(string.ascii_uppercase), LENGTH)
        mutated = np.empty(LENGTH, dtype=str)
        for index, (gene, mutation) in enumerate(zip(self.genes, mutations)):
            if random.random() < self.mutation_probability:
                mutated[index] = mutation
            else:
                mutated[index] = gene
        return Chromosome(mutated)
