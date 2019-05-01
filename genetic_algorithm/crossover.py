import random

import numpy as np

from genetic_algorithm.chromosome import IDEAL_CHROMOSOME, Chromosome


class Crossover:
    def __init__(self, parents, probability=0.98):
        self.parents = parents
        self.probability = probability
        self.pivot = random.randint(0, len(IDEAL_CHROMOSOME))

    def __call__(self):
        if self.will_crossover_happen():
            return self.offspring()
        else:
            return self.parents

    def will_crossover_happen(self):
        return random.random() < self.probability

    def offspring(self):
        a = self.parents[0]
        b = self.parents[1]
        genes_1 = np.concatenate([a.genes[: self.pivot], b.genes[self.pivot :]])
        genes_2 = np.concatenate([b.genes[: self.pivot], a.genes[self.pivot :]])
        return [Chromosome(genes_1), Chromosome(genes_2)]
