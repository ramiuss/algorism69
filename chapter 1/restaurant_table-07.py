total = 100
n = 10

def check(remain, pre) :
  if remain < 0 :
    return 0
  elif remain == 0 :
    return 1
  cnt = 0
  for i in range(pre, n + 1) :
    cnt += check(remain - i, i)
  return cnt

print(check(total, 2))