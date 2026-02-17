def asymetric(N, arr):
    values = []
    for n in range(N):
        asymetrics = []
        l = 0
        r = n
        while r <= N:
            curr = arr[l:r]
            pl = l 
            pr = r
            temp = []
            while pl < pr:
                temp.append(arr[pl] - arr[pr]) 
                pl += 1
                pr -= 1
            l += 1
            r += 1
            asymetrics.append(sum(temp))
        values.append(min(asymetrics))