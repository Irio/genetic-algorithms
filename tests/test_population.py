import string

import numpy as np

from genetic_algorithm.chromosome import Chromosome
from genetic_algorithm.population import Population


def test_init_assigns_chromosomes():
    chromosomes = [
        Chromosome(np.array(list("A" * 26))),
        Chromosome(np.array(list("B" * 26))),
    ]
    subject = Population(chromosomes)
    assert subject.chromosomes == chromosomes


def test_random_parents_returns_two_random_chromosomes():
    chromosomes = [
        Chromosome(np.array(list("A" * 26))),
        Chromosome(np.array(list("B" * 26))),
        Chromosome(np.array(list("C" * 26))),
    ]
    subject = Population(chromosomes)
    random_parents = subject.random_parents()
    assert len(random_parents) == 2
    assert random_parents[0] == chromosomes[0]
    assert random_parents[1] == chromosomes[0]


def test_best_chromosomes_sorts_them_in_descending_order():
    chromosomes = [
        Chromosome(np.array(list("ABCXXXXXXXXXXXXXXXXXXXXXXX"))),
        Chromosome(np.array(list("ABXXXXXXXXXXXXXXXXXXXXXXXX"))),
        Chromosome(np.array(list(string.ascii_uppercase))),
    ]
    subject = Population(chromosomes)
    expected = [chromosomes[2], chromosomes[0], chromosomes[1]]
    assert subject.best_chromosomes() == expected


def test_parents_probabilities_returns_values_proportional_to_their_fitness():
    chromosomes = [
        Chromosome(np.array(list("ABCXXXXXXXXXXXXXXXXXXXXXXX"))),
        Chromosome(np.array(list("ABXXXXXXXXXXXXXXXXXXXXXXXX"))),
        Chromosome(np.array(list(string.ascii_uppercase))),
    ]
    subject = Population(chromosomes)
    result = subject.parents_probabilities()
    expected = [0.12121212, 0.09090909, 0.78787879]
    np.testing.assert_allclose(result, expected)
