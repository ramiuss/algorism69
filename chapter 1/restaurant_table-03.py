total = 6

def graph(untabled, tabled_before) :
    count = 0
    for tabled in range(max(2, tabled_before), min(10, untabled) +1 ) :
        if untabled - tabled == 0 :
            count += 1
        else :
            count += graph(untabled - tabled, tabled)
    return count

print(graph(total, 0))