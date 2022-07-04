from time import perf_counter
import sys

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
start = perf_counter()
result = []
for i in src:
    if src.count(i) == 1:
        result.append(i)
print(result, perf_counter() - start, sys.getsizeof(result))

start = perf_counter()
result = [i for i in src if src.count(i) == 1]
print(result, perf_counter() - start, sys.getsizeof(result))

