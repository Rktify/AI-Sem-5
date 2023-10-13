import random
import math

num_cities = 7
city_names = "ABCDEFG"
starting_city = 0
population_size = 100

class Individual:
    def __init__(self):
        self.path = ""
        self.distance = 0

    def __lt__(self, other):
        return self.distance < other.distance

    def __gt__(self, other):
        return self.distance > other.distance

def random_integer(min_val, max_val):
    return random.randint(min_val, max_val - 1)

def contains_repeated_char(string, char):
    for i in range(len(string)):
        if string[i] == char:
            return True
    return False

def mutate_path(path):
    path = list(path)
    while True:
        random_index_1 = random_integer(1, num_cities)
        random_index_2 = random_integer(1, num_cities)
        if random_index_1 != random_index_2:
            temp = path[random_index_1]
            path[random_index_1] = path[random_index_2]
            path[random_index_2] = temp
            break
    return ''.join(path)

def generate_random_path():
    path = "0"
    while True:
        if len(path) == num_cities:
            path += path[0]
            break
        random_city = random_integer(1, num_cities)
        if not contains_repeated_char(path, str(random_city)):
            path += str(random_city)
    return path

def calculate_distance(path):
    distance_matrix = [
        [0, 12, 10, math.inf, math.inf, math.inf, 12],
        [12, 0, 8, 12, math.inf, math.inf, math.inf],
        [10, 8, 0, 11, 3, math.inf, 9],
        [math.inf, 12, 11, 0, 11, 10, math.inf],
        [math.inf, math.inf, 3, 11, 0, 6, 7],
        [math.inf, math.inf, math.inf, 10, 6, 0, 9],
        [12, math.inf, 9, math.inf, 7, 9, 0]
    ]
    total_distance = 0
    for i in range(len(path) - 1):
        if distance_matrix[int(path[i])][int(path[i + 1])] == math.inf:
            return math.inf
        total_distance += distance_matrix[int(path[i])][int(path[i + 1])]
    return total_distance

def decrease_temperature(temperature):
    return (90 * temperature) / 100

bestFitness = math.inf
bestRoute = ""

city_dict = {
    '0': 'A',
    '1': 'B',
    '2': 'C',
    '3': 'D',
    '4': 'E',
    '5': 'F',
    '6': 'G',
}

def translate(path):
    return '-'.join([city_dict[city] for city in path])

def solve_tsp(x):
    global bestFitness, bestRoute
    generation = 1
    generation_threshold = 100
    population = []

    for i in range(population_size):
        temp_individual = Individual()
        temp_individual.path = generate_random_path()
        temp_individual.distance = calculate_distance(temp_individual.path)
        population.append(temp_individual)

    print("\nInitial population: \nPATH     DISTANCE\n")
    for i in population:
        print(i.path, i.distance)
    print()

    temperature = 10000
    while temperature > 1000 and generation <= generation_threshold:
        population.sort()
        print("\nCurrent temperature: ", temperature)
        new_population = []

        for i in range(population_size):
            parent_1 = population[i]
            while True:
                new_path = mutate_path(parent_1.path)
                new_individual = Individual()
                new_individual.path = new_path
                new_individual.distance = calculate_distance(new_individual.path)
                if new_individual.distance <= parent_1.distance:
                    new_population.append(new_individual)
                    break
                else:
                    probability = pow(2.7, -1 * (float(new_individual.distance - parent_1.distance) / temperature))
                    if probability > 0.5:
                        new_population.append(new_individual)
                        break

        temperature = decrease_temperature(temperature)
        population = new_population
        print("Generation", generation)
        print("PATH     DISTANCE")
        for i in population:
            print(i.path, i.distance)
            if i.distance < bestFitness:
                bestFitness = i.distance
                bestRoute = i.path
                print("Found a better solution!")

        generation += 1

distance_matrix = [
    [0, 12, 10, math.inf, math.inf, math.inf, 12],
    [12, 0, 8, 12, math.inf, math.inf, math.inf],
    [10, 8, 0, 11, 3, math.inf, 9],
    [math.inf, 12, 11, 0, 11, 10, math.inf],
    [math.inf, math.inf, 3, 11, 0, 6, 7],
    [math.inf, math.inf, math.inf, 10, 6, 0, 9],
    [12, math.inf, 9, math.inf, 7, 9, 0]
]

solve_tsp(distance_matrix)

print("--------------------------")
print("Best Route:", translate(bestRoute))
print("Best Fitness Value:", bestFitness)
