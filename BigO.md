# BigO

## Nội dung bài viết

-   [Algorithm Performance](#algorithm-performance)
-   [BigO Notation](#bigo-notation)
-   [BigO Rules](#bigo-rules)
-   [BigO Runtime](#bigo-runtime)
    -   [O(1)](#o1)
    -   [O(log(n))](#ologn)
    -   [O(n)](#on)
    -   [O(n\*log(n))](#onlogn)
    -   [O(n<sup>2</sup>)](#on2)
-   [Time and Space](#time-and-space)

## Algorithm Performance

Một bài toán hay một vấn đề trong lập trình có thể được giải quyết theo nhiều cách _(giải thuật)_ khác nhau. Mỗi cách có ưu nhược điểm và **hiệu suất** _(tốc độ thực thi)_ khác nhau.

Tốc độ thực thi của một _giải thuật_ có thể được đo bằng một bộ đếm thời gian đơn giản. Ví dụ đo tốc độ thực thi trong `Python`:

```python
from timeit import timeit

before_run_test = """
from random import shuffle

_list = [i for i in range(100)]
"""

test_code = """
shuffle(_list)
"""

time = timeit(stmt=test_code, setup=before_run_test)
print(time)
```

Output:

```python
28.090767400000004
```

Sử dụng bộ đếm thời gian có thể hữu ích khi so sánh tốc độ thực tế giữa 2 *giải thuật* khi chạy. Tuy nhiên, bộ đếm thời gian không đáng tin cậy do có rất nhiều yếu tố có thể ảnh hưởng đến tốc độ thực thi của chương trình máy tính như: phần cứng trên các máy tính khác nhau (tốc độ của vi xử lý, RAM, ...), các chương trình khác đang chạy, ...

## BigO Notation

## BigO Rules

## BigO Runtime

### O(1)

### O(log(n))

### O(n)

### O(n\*log(n))

### O(n<sup>2</sup>)
