# 문제 1. 문자열 압축 (난이도: 중)

# 주어진 문자열에서 연속으로 나타나는 문자를 압축해서 표현하세요.
# 예를 들어, 문자열이 "aaabbccccdaa"라면 "a3b2c4d1a2"로 압축됩니다.

# 입력 예시
# "aaabbccccdaa"

a = "aaabbccccdaa"
print(a, a[0])

current_char = a[0]
count = 0
result = []
for i in range(len(a)) :
    if a[i] == current_char :
        count += 1
    else:
        result .append(current_char + str(count))
        current_char = a[i]
        count = 1
result.append(current_char + str(count))        
print(result) 
print(''.join(result))
