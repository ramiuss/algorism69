total = 6
def graph(untabled) :
  print(f'{untabled}person is remained')
  for tabled in range(2, min(10, untabled) + 1) :
    print(f'{tabled}person sitted. {untabled - tabled}person is remained')
    graph(untabled - tabled)
    print(f'Return to {untabled}person)

graph(total) 
    
