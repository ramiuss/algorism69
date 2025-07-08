W = 1000
N = 20

def cut(w, h) :
    if w == h :
        return 1
    if w > h :
        w, h = h, w
    q, r = divmod(h, w)
    result = q
    if r > 0 :
        result += cut(w, r)
    return result


count = 0
for i in range(1, W + 1) :
    for j in range(i, W + 1) :
        if cut(i, j ) == N :
            count += 1

print(count)