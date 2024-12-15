import random
import time
import matplotlib.pyplot as plt

def generate_array(n, max_value, seed):
    random.seed(seed)
    return [random.randint(1, max_value) for _ in range(n)]

def is_unique(array):
    return len(array) == len(set(array))

def measure_execution_time(array):
    start_time = time.time()
    _ = is_unique(array)
    end_time = time.time()
    return (end_time - start_time) * 1000  

n_values = [100, 150, 200, 250, 300, 350, 400, 500]
max_value = 250 - 63  
seed = 42  

worst_case_times = []
average_case_times = []

for n in n_values:
    array = generate_array(n, max_value, seed)

    average_case_time = measure_execution_time(array)
    average_case_times.append(average_case_time)

    worst_case_array = array + array  
    worst_case_time = measure_execution_time(worst_case_array)
    worst_case_times.append(worst_case_time)

with open("worst_avg.txt", "w") as file:
    file.write("n\tAverage Case (ms)\tWorst Case (ms)\n")
    for i, n in enumerate(n_values):
        file.write(f"{n}\t{average_case_times[i]:.2f}\t{worst_case_times[i]:.2f}\n")

plt.figure(figsize=(10, 6))
plt.plot(n_values, average_case_times, label='Average Case', marker='o')
plt.plot(n_values, worst_case_times, label='Worst Case', marker='x')
plt.xlabel('Array Size (n)')
plt.ylabel('Execution Time (ms)')
plt.title('Worst Case vs Average Case Execution Time')
plt.legend()
plt.grid()
plt.savefig("execution_time_plot.jpg")
plt.show()