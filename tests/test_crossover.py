from unittest.mock import MagicMock, patch

import numpy as np

from genetic_algorithm.chromosome import Chromosome
from genetic_algorithm.crossover import Crossover


def test_call_returns_parents_if_must_not_crossover(monkeypatch):
    parents = [Chromosome.random(), Chromosome.random()]
    subject = Crossover(parents)
    monkeypatch.setattr(subject, "will_crossover_happen", lambda: False)
    assert subject() == parents


def test_call_returns_crossed_over_if_must_crossover(monkeypatch):
    parents = [Chromosome.random(), Chromosome.random()]
    subject = Crossover(parents)
    monkeypatch.setattr(subject, "will_crossover_happen", lambda: True)
    assert subject() == subject.offspring()


@patch("genetic_algorithm.crossover.random.random")
def test_will_crossover_happen_returns_true_if_random_is_less_than_probability(random):
    parents = [Chromosome.random(), Chromosome.random()]
    subject = Crossover(parents, probability=0.8)
    random.return_value = 0.7
    assert subject.will_crossover_happen()


@patch("genetic_algorithm.crossover.random.random")
def test_will_crossover_happen_returns_false_if_random_is_greater_than_probability(
    random
):
    parents = [Chromosome.random(), Chromosome.random()]
    subject = Crossover(parents, probability=0.8)
    random.return_value = 0.9
    assert not subject.will_crossover_happen()


def test_offspring_returns_two_chromosomes_combining_parents():
    parents = [Chromosome.random(), Chromosome.random()]
    subject = Crossover(parents)
    result = subject.offspring()
    assert len(result) == 2
    assert isinstance(result[0], Chromosome)
    assert isinstance(result[1], Chromosome)


def test_offspring_returns_chromosomes_combining_parents(monkeypatch):
    parents = [
        Chromosome(np.array(list("XXXXXXXXXXXXXXXXXXXXXXXXXX"))),
        Chromosome(np.array(list("YYYYYYYYYYYYYYYYYYYYYYYYYY"))),
    ]
    subject = Crossover(parents)
    monkeypatch.setattr(subject, "pivot", 3)
    result = subject.offspring()
    assert result[0] == Chromosome(np.array(list("XXXYYYYYYYYYYYYYYYYYYYYYYY")))
    assert result[1] == Chromosome(np.array(list("YYYXXXXXXXXXXXXXXXXXXXXXXX")))
