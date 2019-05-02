import string
from unittest.mock import patch

import numpy as np

from genetic_algorithm.chromosome import Chromosome

GENES_FIXTURE = np.array(list("SVaddNjtvYKxgyymbMNxUyrLzn"))


def test_init_assigns_genes():
    subject = Chromosome(GENES_FIXTURE)
    assert np.array_equal(subject.genes, GENES_FIXTURE)


def test_random_generates_genes():
    subject = Chromosome.random()
    assert isinstance(subject, Chromosome)
    assert np.array_equal(subject.genes, GENES_FIXTURE)


def test_fitness_returns_chromosome_length_for_ideal_result():
    subject = Chromosome(np.array(list(string.ascii_uppercase)))
    assert subject.fitness() == 26


def test_fitness_returns_number_of_correct_genes():
    subject = Chromosome(np.array(list("ABXXXXXXXXXXXXXXXXXXXXXXXX")))
    assert subject.fitness() == 3


@patch("genetic_algorithm.chromosome.random.random")
def test_mutated_generates_genes(random):
    random.side_effect = [0.01, 0.01] + [1] * 24
    subject = Chromosome(np.array(list(string.ascii_uppercase)))
    result = subject.mutated()
    expected = Chromosome(np.array(list("IJCDEFGHIJKLMNOPQRSTUVWXYZ")))
    assert isinstance(result, Chromosome)
    assert result == expected
