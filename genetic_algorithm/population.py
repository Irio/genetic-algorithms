import numpy as np

from genetic_algorithm.chromosome import Chromosome


class Population:
    def __init__(self, chromosomes):
        self.chromosomes = chromosomes

    def random_parents(self):
        parents = np.random.choice(
            self.chromosomes, 2, replace=True, p=self.parents_probabilities()
        )
        return list(parents)

    def best_chromosomes(self):
        return sorted(self.chromosomes)[::-1]

    def parents_probabilities(self):
        get_fitness = np.vectorize(lambda x: x.fitness())
        probabilities = get_fitness(self.chromosomes)
        return probabilities / probabilities.sum()
