import time
start_tiem = time.time()

total = 100
memo = {}
def graph(untabled, tabled_before) :
    if (untabled, tabled_before) in memo :
        return memo[(untabled, tabled_before)]
    count = 0
    for tabled in range(max(2, tabled_before), min(10, untabled) + 1 ) :
        if untabled - tabled == 0 :
            count += 1
        else :
            count += graph(untabled - tabled, tabled)
    memo[(untabled, tabled_before)] = count
    return count

print(graph(total, 0))

end_time = time.time()
print(f'Excution time: {end_time - start_tiem:.6f} seconds')
