import random
import numpy as np

# 全体集合Uの要素数
n = 100
# 部分集合の数
N = 1000
# ハイパーパラメーター
A = 10
B = 1

def H_A_sigma(a, xl):
    sum = 0
    for i in range(N):
        if a in subsets[i]:
            sum += xl[i]
    return sum

def H_A(xl):
    return A * sum((1 - H_A_sigma(a, xl)) ** 2 for a in range(1, n + 1))

def H_B(xl):
    return B * sum(xl[i] for i in range(N))

def energy_function(xl):
    return H_A(xl) + H_B(xl)

def count_uncovered_elements(xl):
    covered_elements = set()
    for i in range(N):
        if xl[i] == 1:
            covered_elements.update(subsets[i])
    return len(U - covered_elements)

def simulated_annealing(initial_temperature, cooling_rate, max_iterations):
    current_solution = [random.randint(0, 1) for _ in range(N)]
    current_energy = energy_function(current_solution)
    temperature = initial_temperature
    
    best_solution = current_solution[:]
    best_energy = current_energy

    for iteration in range(max_iterations):
        if temperature <= 0:
            break
        
        new_solution = current_solution[:]
        flip_index = random.randint(0, N - 1)
        new_solution[flip_index] = 1 - new_solution[flip_index]  # Flip the bit
        
        new_energy = energy_function(new_solution)
        
        if new_energy < current_energy or random.random() < np.exp((current_energy - new_energy) / temperature):
            current_solution = new_solution[:]
            current_energy = new_energy
        
        if new_energy < best_energy:
            best_solution = new_solution[:]
            best_energy = new_energy
        
        temperature *= cooling_rate
    
    return best_solution, best_energy

# Uと部分集合の読み込み
U = set(range(1, n + 1))  # Uの例
subsets = [
    set(random.sample(U, random.randint(1, 10))) for _ in range(N)
]

# 焼きなまし法のパラメータ
initial_temperature = 100.0
cooling_rate = 0.99
max_iterations = 10000

best_solution, best_energy = simulated_annealing(initial_temperature, cooling_rate, max_iterations)
uncovered_elements = count_uncovered_elements(best_solution)

print("部分集合の集合: ", subsets)
print("最適な部分集合の組み合わせ: ", best_solution)
print("被覆されていない要素の数: ", uncovered_elements)
print("H: ", best_energy)
print("選ばれた部分集合の数: ", sum(best_solution))