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


import time
from functools import lru_cache
start_time = time.time()

total = 100
@lru_cache(maxsize=None)
def graph(untabled, tabled_before) :
    count = 0
    for tabled in range(max(2, tabled_before), min(10, untabled) + 1 ) :
        if untabled - tabled == 0 :
            count += 1
        else :
            count += graph(untabled - tabled, tabled)
    return count

print(graph(total, 0))

end_time = time.time()
print("Execution time:", end_time - start_time, "seconds")