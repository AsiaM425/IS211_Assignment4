import time
import random

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr

def python_sort(arr):
    return sorted(arr)

def main():
    sizes = [500, 1000, 10000]
    for size in sizes:
        avg_insertion_sort_time = 0
        avg_shell_sort_time = 0
        avg_python_sort_time = 0
        for i in range(100):
            arr = [random.randint(0, 1000) for _ in range(size)]

            start_time = time.time()
            insertion_sort(arr)
            end_time = time.time()
            avg_insertion_sort_time += end_time - start_time

            start_time = time.time()
            shell_sort(arr)
            end_time = time.time()
            avg_shell_sort_time += end_time - start_time

            start_time = time.time()
            python_sort(arr)
            end_time = time.time()
            avg_python_sort_time += end_time - start_time

        avg_insertion_sort_time /= 100
        avg_shell_sort_time /= 100
        avg_python_sort_time /= 100

        print(f"Insertion Sort took {avg_insertion_sort_time:.2f} seconds to run, on average")
        print(f"Shell Sort took {avg_shell_sort_time:.2f} seconds to run, on average")
        print(f"Python Sort took {avg_python_sort_time:.2f} seconds to run, on average")

if __name__ == "__main__":
    main()
