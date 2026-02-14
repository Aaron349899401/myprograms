def can_ride(N, C, P):
    return "NO" if N % (C * P) > 0 else "YES"

