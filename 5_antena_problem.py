def initialize_chromosomes():
    chromosome1 = [(2, 3), (2, 4), (2, 5), (5, 2), (5, 5)]
    chromosome2 = [(2, 3), (3, 5), (2, 6), (5, 3), (5, 5)]
    chromosome3 = [(2, 2), (1, 4), (3, 5), (4, 6), (5, 6)]    

    chromosomes = [chromosome1, chromosome2, chromosome3]
    return chromosomes


def compute_fitness(chromosome):
    covered_squares = []
    for position in chromosome:
        x, y = position
        if (x, y) not in covered_squares:
            covered_squares.append((x, y))
        if x - 1 >= 1 and (x - 1, y) not in covered_squares:
            covered_squares.append((x - 1, y))  # Left
        if x + 1 <= 6 and (x + 1, y) not in covered_squares:
            covered_squares.append((x + 1, y))  # Right
        if y - 1 >= 1 and (x, y - 1) not in covered_squares:
            covered_squares.append((x, y - 1))  # Up
        if y + 1 <= 6 and (x, y + 1) not in covered_squares:
            covered_squares.append((x, y + 1))  # Down

    return len(covered_squares)

def crossover(parent1, parent2):
    crossover_point = 3
    offspring = parent1[:crossover_point] + parent2[crossover_point:]
    return offspring

def mutate(chromosome):
    i = 0
    for position in chromosome:
        x, y = position
        if y > 1:
            chromosome[i] = (x, y-1)
        i += 1

    return chromosome

def sort_by_fitness(chromosomes, fitness_values):
    combined_data = []
    for i in range(len(chromosomes)):
        combined_data.append((chromosomes[i], fitness_values[i]))

    sorted_data = sorted(combined_data, key=lambda x: x[1], reverse=True)

    sorted_chromosomes = []
    sorted_fitness_values = []
    for data in sorted_data:
        sorted_chromosomes.append(data[0])
        sorted_fitness_values.append(data[1])

    return sorted_chromosomes, sorted_fitness_values



def ga():
    #genwration 1
    chromosomes = initialize_chromosomes()
    fitness_values_1 = [compute_fitness(chromosome) for chromosome in chromosomes]
    sorted_chromosomes_1, sorted_fitness_1 = sort_by_fitness(chromosomes, fitness_values_1)


    # genration 2 croosover
    offspring1 = crossover(sorted_chromosomes_1[1], sorted_chromosomes_1[2])
    offspring2 = crossover(sorted_chromosomes_1[2], sorted_chromosomes_1[1])
    sorted_chromosomes_1[1] = offspring1
    sorted_chromosomes_1[2] = offspring2
    fitness_values_2 = [compute_fitness(chromosome) for chromosome in sorted_chromosomes_1]
    sorted_chromosomes_2, sorted_fitness_2 = sort_by_fitness(sorted_chromosomes_1, fitness_values_2)

    #generation 2 mutation
    min_fitness_index = sorted_fitness_2.index(min(sorted_fitness_2))
    sorted_chromosomes_2[min_fitness_index] = mutate(sorted_chromosomes_2[min_fitness_index])
    fitness_values_3 = [compute_fitness(chromosome) for chromosome in sorted_chromosomes_2]
    sorted_chromosomes_3, sorted_fitness_3 = sort_by_fitness(sorted_chromosomes_2,fitness_values_3)

    #generation 3
    offspring1 = crossover(sorted_chromosomes_3[1], sorted_chromosomes_3[2])
    offspring2 = crossover(sorted_chromosomes_3[2], sorted_chromosomes_3[1])
    sorted_chromosomes_3[1] = offspring1
    sorted_chromosomes_3[2] = offspring2
    fitness_values_4 = [compute_fitness(chromosome) for chromosome in sorted_chromosomes_3]
    sorted_chromosomes_4, sorted_fitness_4 = sort_by_fitness(sorted_chromosomes_3, fitness_values_4)
    return sorted_chromosomes_4, sorted_fitness_4

# Example usage
solution,fitness = ga()
print("Solution:")
for i in range ((len(solution))):
    print(solution[i])

print("fitness values :", fitness)