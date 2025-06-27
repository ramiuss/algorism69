# n = 4 

# result = []
# for i in range(n + 1) :
#     for j in range(n + 1) :
#         k = n - (i + j)
#         if k >= 0 :
#             print(i, j, k)
#             result.append((i, j, k))

# # 이제 한 번의 경우에 승부가 나는 경우의 수를 카운트 해 보자

# count = 0
# for i in result :
#     if i[0] > i[1] and i[0] > i[2] :
#         count += 1
#         print(f'가위 {i[0]}, 바위 {i[1]},  보자기 {i[2]}.. 가위 승')
#     if i[1] > i[0] and i[1] > i[2] :
#         count += 1
#         print(f'가위 {i[0]}, 바위 {i[1]},  보자기 {i[2]}.. 바위 승')
#     if i[2] > i[0] and i[2] > i[1] :
#         count += 1
#         print(f'가위 {i[0]}, 바위 {i[1]},  보자기 {i[2]}.. 보자기 승')

# print(f'한 번에 승부가 결정 나는 경우의 수는 {count}')


# 책에서 풀이를 어떻게 하는지 보자..

# n = 4

# count = 0
# for rock in range(0, n + 1) :
#     for scissors in range(0, n - rock + 1) :
#         paper = n - rock - scissors
#         all = [rock, scissors, paper]
#         print(all)
#         if all.count(max(all)) == 1 :
#             count += 1

# print(count) 

# 조합을 사용해서 푸는 방법
n = 4
count = 0
for l in range(0, n + 1) :
    for r in range(l, n + 1) :
        all = [l, r - l, n - r]  # 왼쪽에서 부터 l(가위를 내고 바위를 낸 사이의 구분) 만큼 이동하면 r(바위를 낸 사이의 구분) 만큼 이동하고, n - r 만큼 보자기를 낸다.
        print(all)
        if all.count(max(all)) == 1 :
            count += 1

print(count)