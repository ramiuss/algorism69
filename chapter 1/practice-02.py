# 문제 5. 가장 긴 연속 부분 수열의 합 (난이도: 상)
# 정수 리스트가 주어질 때, 연속된 부분 수열 중 합이 가장 큰 값을 구하세요.
# (예: 카데인 알고리즘)

# 입력 예시
# nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

# 출력 예시
# 6
# (부분 수열: [4, -1, 2, 1])

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

current_max = 0
for i in range(len(nums)) :
    result = 0
    for j in range(i, len(nums)) :
        result += nums[j]
        if result > current_max :
            current_max = result
        print(f'{nums[i : j + 1]} ->{result}')

print(f'max_sum = {current_max}')


