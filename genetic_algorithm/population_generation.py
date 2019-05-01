import os

from genetic_algorithm.chromosome import Chromosome
from genetic_algorithm.crossover import Crossover
from genetic_algorithm.population import Population


class PopulationGeneration:
    SIZE = 100

    def __init__(self, previous_generation=None, etilism_percentage=0.1):
        self.etilism_percentage = etilism_percentage
        self.previous_generation = previous_generation

    def __call__(self):
        if self.previous_generation is None:
            return self.first_generation()
        else:
            return self.evolve_previous_generation()

    def first_generation(self):
        chromosomes = []
        for _ in range(self.SIZE):
            chromosomes.append(Chromosome.random())
        return Population(chromosomes)

    def evolve_previous_generation(self):
        number_of_candidates_to_maintain = round(self.SIZE * self.etilism_percentage)
        next_generation = self.etilist_candidates()
        for _ in range(self.n_crossovers):
            parents = self.previous_generation.random_parents()
            offspring = Crossover(parents)()
            for chromosome in offspring:
                next_generation.append(chromosome.mutated())
        return Population(next_generation)

    def etilist_candidates(self):
        return self.previous_generation.best_chromosomes()[: self.n_etilists]

    @property
    def n_etilists(self):
        return round(self.SIZE * self.etilism_percentage)

    @property
    def n_crossovers(self):
        return round((100 - self.n_etilists) / 2)
