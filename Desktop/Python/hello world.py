def addsum(s):
    nums = 0
    s = s.split()
    for i in range(len(s)):
        nums += int(s[i])
    return nums
print(addsum(input()))
