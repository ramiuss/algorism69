#디지탈 시계는 7개의 칸에 불을 켜서 숫자를 표현한다.
#각 칸은 다음과 같이 표현된다.

memo = {0: 6, 1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6}

count = 0
for i in range(24) :
    # print(i // 10, i % 10)
    # print(memo[i // 10], memo[i % 10])
    hour_count = memo[i // 10] + memo[i % 10]
    # print(f'{i}시는 디지탈 세그먼트 {hour_count}개를 켜야 합니다.') 

    for j in range(60) :
        # print(j // 10, j % 10)
        # print(memo[j // 10], memo[j % 10])
        minute_count = memo[j // 10] + memo[j % 10]
        # print(f'{i}시 {j}분은 디지탈 세그먼트 {hour_count + minute_count}개를 켜야 합니다.')

        for k in range(60) :
            # print(k // 10, k % 10)
            # print(memo[k // 10], memo[k % 10])
            second_count = memo[k // 10] + memo[k % 10]
            # print(f'{i}시 {j}분 {k}초는 디지탈 세그먼트 {hour_count + minute_count + second_count}개를 켜야 합니다.')
            sum_count = hour_count + minute_count + second_count
            if sum_count == 30 :
                count += 1

print(f'디지탈 시계에서 30개의 세그먼트를 켜는 경우는 총 {count}가지입니다.')



N = 30

def check(num) :
    light = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
    return light[num // 10] + light[num % 10]

count = 0
for i in range(24) :
    for j in range(60) :
        for k in range(60) :
            if check(i) + check(j) + check(k) == N :
                count += 1

print(f'디지탈 시계에서 {N}개의 세그먼트를 켜는 경우는 총 {count}가지입니다.')