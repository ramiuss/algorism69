n = 3

def hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    hanoi(n - 1, source, auxiliary, target)
    print(f"Move disk {n} from {source} to {target}")
    hanoi(n - 1, auxiliary, target, source)
    print(f'Complted moving {n} disks from {source} to {target} using {auxiliary}')

hanoi(n, 'A', 'C', 'B')