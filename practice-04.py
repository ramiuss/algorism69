# 새로운 파이썬 알고리즘 문제

# 문제: 연속된 부분수열의 곱이 K 이하인 경우의 수

# 정수로 이루어진 리스트 nums와 정수 K가 주어집니다.
# 리스트에서 연속된 부분수열(길이 1 이상)의 곱이 K 이하인 경우가 몇 개인지 구하세요.

#     부분수열은 반드시 연속되어야 합니다.

#     각 부분수열의 곱이 K 이하일 때만 카운트합니다.

#     nums의 길이는 1 이상 10,000 이하, 각 원소는 1 이상 100 이하의 정수입니다.

#     K는 1 이상 10^9 이하의 정수입니다.

# nums = [10, 5, 2, 6]
# K = 100

# count = 0
# for i in range(len(nums)) :
#     result = 1
#     for j in range(i, len(nums)) :
#         result *= nums[j]
#         if result <= K :
#             count += 1
#         print(f'{nums[i : j + 1]} -> {result}, count : {count}')

# print(f'부분수열의 곱이 {K} 이하인 경우의 수: {count}')



import random

nums_2 = []
for i in range(10) :
    a = random.randrange(100)
    nums_2.append(a)

print(nums_2)
K = 100

def count_subsequences(nums, K):
    count = 0 
    for i in range(len(nums_2)) :
        result_2 = 1
        for j in range(i, len(nums_2)) :
            result_2 *= nums[j]
            if result_2 <= K :
                count += 1
            print(f'{nums_2[i : j + 1]} -> {result_2}, count : {count}')
    return count

print(f'부분수열의 곱이 {K} 이하인 경우의 수: {count_subsequences(nums_2, K)}')
