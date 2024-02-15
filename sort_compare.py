import time
import random

def insertion_sort(alist):
    start_time = time.time()
    for index in range(1, len(alist)):
        current_value = alist[index]
        position = index

        while position > 0 and alist[position - 1] > current_value:
            alist[position] = alist[position - 1]
            position = position - 1

        alist[position] = current_value

    end_time = time.time()
    return alist, end_time - start_time

def shell_sort(alist):
    start_time = time.time()
    sublist_count = len(alist) // 2

    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(alist, start_position, sublist_count)

        sublist_count = sublist_count // 2

    end_time = time.time()
    return alist, end_time - start_time

def gap_insertion_sort(alist, start, gap):
    for i in range(start + gap, len(alist), gap):
        current_value = alist[i]
        position = i

        while position >= gap and alist[position - gap] > current_value:
            alist[position] = alist[position - gap]
            position = position - gap

        alist[position] = current_value

def python_sort(alist):
    start_time = time.time()
    sorted_list = sorted(alist)
    end_time = time.time()
    return sorted_list, end_time - start_time

def main():
    list_sizes = [500, 1000, 5000]
    avg_times = {'Insertion Sort': 0, 'Shell Sort': 0, 'Python Sort': 0}

    for size in list_sizes:
        for _ in range(100):
            random_list = random.sample(range(1, 10000), size)

            _, insertion_time = insertion_sort(random_list.copy())
            _, shell_time = shell_sort(random_list.copy())
            _, python_sort_time = python_sort(random_list.copy())

            avg_times['Insertion Sort'] += insertion_time
            avg_times['Shell Sort'] += shell_time
            avg_times['Python Sort'] += python_sort_time

    for algo, time_taken in avg_times.items():
        avg_time = time_taken / 100
        print(f"{algo} took {avg_time:10.7f} seconds to run, on average")

if __name__ == "__main__":
    main()
# Write your code here :-)
