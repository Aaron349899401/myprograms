def speed(arr): # CORRECT!
    arr.sort(key=lambda x: x[0])
    speeds = []
    for i in range(1, len(arr)):
        time = arr[i][0] - arr[i - 1][0]
        distance = arr[i][1] - arr[i - 1][1]
        speeds.append(abs(distance) / time)
    
    return max(speeds)

N = int(input())
arr = [tuple(map(int, input().split())) for _ in range(N)]

print(speed(arr))