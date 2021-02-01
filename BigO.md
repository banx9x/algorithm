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

Sử dụng bộ đếm thời gian có thể hữu ích khi so sánh tốc độ thực tế giữa 2 _giải thuật_ khi chạy. Tuy nhiên, bộ đếm thời gian không đáng tin cậy do có rất nhiều yếu tố có thể ảnh hưởng đến tốc độ thực thi của chương trình máy tính như: phần cứng trên các máy tính khác nhau (tốc độ của vi xử lý, RAM, ...), các chương trình khác đang chạy, ngôn ngữ lập trình được sử dụng, ...

## BigO Notation

`BigO` là một ký hiệu toán học được sử dụng trong Khoa học Máy tính (Computer Science) để mô tả hiệu suất hoặc độ phức tạp của một thuật toán _(trên lý thuyết)_. `BigO` chỉ ra giới hạn gần đúng _(tiệm cận)_ về thời gian thực thi thuật toán dựa trên kích thước của tập dữ liệu được sử dụng.

Nói cách khác, `BigO` không cho biết tốc độ thực thi của một thuật toán với thời gian cụ thể, mà nó cho biết số lượng phép toán mà chúng cần thực hiện, đồng thời thể hiện hiệu suất của thuật toán khi kích thước dữ liệu đầu vào thay đổi

Tìm hiểu thêm về khái niệm `BigO` tại đây: [wiki/Big_O_Notation](https://en.wikipedia.org/wiki/Big_O_notation)

## BigO Rules

Thử hình dung với một ví dụ đơn giản:

Khi giải một bài tập thầy **Ba** giao, bạn tìm kiếm Google để tìm lời giải. Các thao tác bạn cần thực hiện:

-   Đọc đề bài (1)
-   Google giải pháp (2)
-   Chép vào và không thèm chạy thử (3)
-   Nộp bài (4)

Với ví dụ này, bạn mất 4 thao tác để hoàn thành => `O(4)`

Nhưng khi số lượng bài tập tăng lên, 10, 20, hay 1000 (`n` bài tập), tổng thao tác bạn cần thực hiện tương ứng => `O(4*n)`

Số thao tác để giải mỗi bài tập không đổi là 4, được gọi là hằng số (`constant`), số lượng bài tập là tập dữ liệu đầu vào (`n`), vậy, tổng số lượng thao tác của bạn phụ thuộc vào `n`

`BigO` tập trung vào các giá trị quan trọng ảnh hưởng tới hiệu suất của thuật toán, loại bỏ các thành phần không quan trọng (hay không đáng kể)

-   Các giá trị hằng số được thay bằng 1
-   Các giá trị nhỏ hơn được bỏ qua

Với ví dụ trên, độ phức tạp sẽ là `O(4*n) => O(n)`

Một số ví dụ khác:

-   O(999999) => O(1)
-   O(10000\*n) => O(n)
-   O(500\* n<sup>2</sup>) => O(n<sup>2</sup>)
-   O(n<sup>2</sup> + 10000\*n + 99999) => O(n<sup>2</sup>)
-   O(n\*log(n) + n + 111) => O(n\*log(n))

## BigO Runtime

Phân tích thuật toán cụ thể với `BigO`

### O(1)

### O(log(n))

### O(n)

### O(n\*log(n))

### O(n<sup>2</sup>)

## Time and Space

`BigO` không chỉ được sử dụng để mô tả tốc độ, hay thời gian chạy của một thuật toán _(độ phức tạp thời gian)_, mà còn được sử dụng để mô tả không gian bộ nhớ _(độ phức tạp về bộ nhớ)_ của thuật toán

Độ phức về không gian tập trung vào phần bộ nhớ phụ trợ (cần thêm), không tính bộ nhớ dành cho chính tập dữ liệu đầu vào.

Ví dụ nhỏ xíu:

```python
def sum(list):
    total = 0
    for i in list:
        total += i
    return total
```

Bất kể số lượng phần tử trong `list` là bao nhiêu, thuật toán trên cũng chỉ yêu cầu thêm 1 _đơn vị bộ nhớ_ dành cho biến `total`, vậy, _độ phức tạp không gian_ là `O(1)`

Ví dụ khác mới làm chiều nay:

```python
def remove_falsy(list):
    result = []
    for i in list:
        if not bool(i): # lại còn bool
            result.append(i)
    return result
```

Với `n` phần tử trong `list` đầu vào, thuật toán yêu cầu `n` _đơn vị bộ nhớ_ bổ sung (trong trường hợp xấu nhất), vậy _độ phức tạp không gian_ là `O(n)`
