N = int(input("Len : "))
Arr = list(map(int, input("array : ").split()))

left = 0
right = N - 1

while left < right:
    while Arr[left] == 0 and left < right:
        left += 1
    while Arr[right] == 1 and left < right:
        right -= 1
    if left < right:
        Arr[left] = 0
        Arr[right] = 1
        left += 1
        right -= 1

print(Arr)