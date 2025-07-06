# n = 0                                                  1
# n = 1                                               1     1
# n = 2                                            1     2     1
# n = 3                                         1     3     3     1
# n = 4                                      1     4     6     4     1
# n = 5                                   1     5    10    10     5    1
# n = 6                                1     6    15    20    15     6    1
# n = 7                             1     7   21    35    35    21     7    1
# n = 8                          1     8   28    56    70    56    28     8    1
# n = 9                       1     9   36    84    126   126   84    36    9    1

# n = 45 일 때를 구하보자

def pascal_triangle(n):
    if n == 0 :
        return [1]
    row = [1]
    for i in range(1, n + 1) :
        new_row = [1]
        for j in range(1, len(row)) :
            new_row.append(row[j - 1] + row[j])
        new_row.append(1)
        row = new_row
    return row

print(pascal_triangle(0))  # [1]
print(pascal_triangle(1))  # [1, 1]
print(pascal_triangle(2))  # [1, 2, 1]
print(pascal_triangle(3))  # [1, 3, 3, 1]
print(pascal_triangle(4))  # [1, 4, 6, 4, 1]
# print(pascal_triangle(45))  

# 사용할 동전은 1원 5원 10원 50원 100원 500원
# 사용할 지폐는 1000원 5000원 10000원 


memo = {10000 : '', 5000 : '', 1000: '', 500 : '', 100 : '', 50 : '',
        10 : '', 5 : '', 1 : ''}
print(len(memo))
print((memo.keys()), type(memo.keys()))  # 리스트로 만들려면 리스트 함수를 사용해야 한다..
print(list(memo.keys())[5])  # [10000, 5000, 1000, 500, 100, 50, 10, 5, 1]


count = 0
for i in pascal_triangle(45):
    for j in range(len(memo)):
        while i >= list(memo.keys())[j] :
            count += i // list(memo.keys())[j]
            i = i % list(memo.keys())[j]

print(count)

