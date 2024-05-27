def finalValueAfter(arr):
    count = 0
    for i in arr:
        if i == "--X" or i == "X--":
            count -= 1
        else:
            count += 1
    return count

arr=["--X","X++","X++"]
print(finalValueAfter(arr))