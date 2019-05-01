from genetic_algorithm.chromosome import LENGTH as CHROMOSOME_LENGTH
from genetic_algorithm.population_generation import PopulationGeneration


class Runner:
    def __init__(self):
        self.first_generation = None
        self.last_generation = None
        self.population = None

    def __call__(self, iterations):
        for times_run in range(iterations):
            self.population = PopulationGeneration(self.population)()
            best_chromosomes = self.population.best_chromosomes()
            position = str(times_run + 1).zfill(3)
            message = f"Run #{position} - {best_chromosomes[0]} - {best_chromosomes[0].fitness()}"
            print(message)

            if times_run == 0:
                self.first_generation = self.population
            if best_chromosomes[0].fitness() == CHROMOSOME_LENGTH:
                break

        self.last_generation = self.population
        self.print_generation(self.first_generation, "First generation")
        self.print_generation(self.last_generation, "Last generation")

    def print_generation(self, population, title):
        print(f"\n{title}:")
        best_chromosomes = population.best_chromosomes()
        for index, chromosome in enumerate(best_chromosomes[:10]):
            position = str(index + 1).zfill(2)
            print(f"{position} - {chromosome} - fitness={chromosome.fitness()}")


if __name__ == "__main__":
    Runner()(iterations=500)
