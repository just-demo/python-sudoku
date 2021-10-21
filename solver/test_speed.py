import os
import time
from format import *
from solver import Solver


def count_lines(file):
    return len(list_lines(file))


def list_lines(file):
    with open(file, 'r') as f:
        return [line for line in f.read().split('\n') if line]


ready_dir = os.path.join(os.getcwd(), os.pardir, 'data/ready')
files = sorted([os.path.join(ready_dir, file) for file in os.listdir(ready_dir)])
counts = {os.path.basename(file): count_lines(file) for file in files}
count = sum(list(counts.values()))
print(files)
print(counts)
print(f'Total count: {count}')

start = time.time_ns()
counter = 0
statistics = {}
for file in files:
    file_start = time.time_ns()
    file_count = 0
    for line in list_lines(file):
        print(line)
        counter += 1
        file_count += 1
        if counter % 2 == 0:
            print(f'progress: {counter} / {(time.time_ns() - start) / 1000000000}s')
        if counter > 10:
            raise Exception('stopped')
        sudoku = sudoku_from_1d_string(line)
        Solver(sudoku).solve()
    statistics[os.path.basename(file)] = (file_count, time.time_ns() - file_start)
print(f'Total time: {time.time_ns() - start / 1000000000}s')
for file, stat in statistics.items():
    print(f'{file}: {stat[1]} / {stat[1] / stat[0]}')
