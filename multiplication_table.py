import math
from tabulate import tabulate

data = []

for i in range(1,10):
    row = []
    for j in range(1,10):
        row.append(f"{j} X {i} = {i * j}")
    data.append(row)

headers = [f"{i}단" for i in range(1,10)]

table = tabulate(data, headers=headers, tablefmt="grid", colalign=("center",) * len(headers))

#헤더 정렬을 잡으려해도 잘 안 되네요... 죄송합니다
print(table)