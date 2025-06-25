total = 6
def graph(untabled) :
#   print(f'{untabled}person is remained')
    count = 0
    for tabled in range(2, min(10, untabled) + 1) :
        # print(f'{tabled}person sitted. {untabled - tabled}person is remained')
        if untabled - tabled == 0 :
            count += 1
            # print(f'All person sitted. Add count +1')
        else :
            count += graph(untabled - tabled)
        # print(f'Return to {untabled}person')

    return count

print(graph(total))

    
