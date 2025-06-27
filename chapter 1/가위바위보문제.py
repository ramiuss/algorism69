n = 4 

result = []
for i in range(n + 1) :
    for j in range(n + 1) :
        k = n - (i + j)
        if k >= 0 :
            print(i, j, k)
            result.append((i, j, k))

# 이제 한 번의 경우에 승부가 나는 경우의 수를 카운트 해 보자

count = 0
for i in result :
    if i[0] > i[1] and i[0] > i[2] :
        count += 1
        print(f'가위 {i[0]}, 바위 {i[1]},  보자기 {i[2]}.. 가위 승')
    if i[1] > i[0] and i[1] > i[2] :
        count += 1
        print(f'가위 {i[0]}, 바위 {i[1]},  보자기 {i[2]}.. 바위 승')
    if i[2] > i[0] and i[2] > i[1] :
        count += 1
        print(f'가위 {i[0]}, 바위 {i[1]},  보자기 {i[2]}.. 보자기 승')

print(f'한 번에 승부가 결정 나는 경우의 수는 {count}')