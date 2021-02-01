from timeit import timeit

test_code = """
_list = [i for i in range(10)]
"""

time = timeit(stmt=test_code)
print(time)

test_code = """
_list = []

for i in range(10):
    _list.append(i)
"""

time = timeit(stmt=test_code)
print(time)
