import random
import time

def sequential_search(lst, elem):
    start = time.time()
    for i in lst:
        if i == elem:
            end = time.time()
            return True, end - start
    end = time.time()
    return False, end - start

def ordered_sequential_search(lst, elem):
    lst.sort()
    start = time.time()
    for i in lst:
        if i == elem:
            end = time.time()
            return True, end - start
        if i > elem:
            end = time.time()
            return False, end - start
    end = time.time()
    return False, end - start

def binary_search_iterative(lst, elem):
    lst.sort()
    start = time.time()
    first = 0
    last = len(lst) - 1
    found = False
    while first <= last and not found:
        midpoint = (first + last) // 2
        if lst[midpoint] == elem:
            found = True
            end = time.time()
        else:
            if elem < lst[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    if found:
        return True, end - start
    else:
        end = time.time()
        return False, end - start

def binary_search_recursive(lst, elem):
    lst.sort()
    start = time.time()
    if len(lst) == 0:
        end = time.time()
        return False, end - start
    else:
        midpoint = len(lst) // 2
        if lst[midpoint] == elem:
            found = True
            end = time.time()
            return True, end - start
        else:
            if elem < lst[midpoint]:
                return binary_search_recursive(lst[:midpoint], elem)
            else:
                return binary_search_recursive(lst[midpoint + 1:], elem)

def main():
    for size in [500, 1000, 10000]:
        print(f"List size: {size}")
        seq_total_time = 0
        ord_seq_total_time = 0
        binary_iter_total_time = 0
        binary_recur_total_time = 0
        for i in range(100):
            lst = [random.randint(1, 100000) for _ in range(size)]
            _, seq_time = sequential_search(lst, -1)
            seq_total_time += seq_time
            _, ord_seq_time = ordered_sequential_search(lst, -1)
            ord_seq_total_time += ord_seq_time
            _, binary_iter_time = binary_search_iterative(lst, -1)
            binary_iter_total_time += binary_iter_time
            _, binary_recur_time = binary_search_recursive(lst, -1)
            binary_recur_total_time += binary_recur_time
        print(f"Sequential search took {seq_total_time/100:.4f} seconds to run, on average")
        print(f"Ordered sequential search took {ord_seq_total_time/100:.4f} seconds to run, on average")
        print(f"Binary search (iterative) took {binary_iter_total_time/100:.4f} seconds to run, on average")
        print(f"Binary search (recursive) took {binary_recur_total_time/100:.4f} seconds to run, on average")

if __name__ == '__main__':
    main()
