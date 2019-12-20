#!/usr/bin/python3
def roman_to_int(roman_string):
    nums = []
    for i in roman_string:
        if i == "I":
            nums.append(1)
        elif i == "V":
            nums.append(5)
        elif i == "X":
            nums.append(10)
        elif i == "L":
            nums.append(50)
        elif i == "C":
            nums.append(100)
        elif i == "D":
            nums.append(500)
        elif i == "M":
            nums.append(1000)

    fnums = []
    i = len(nums) - 1
    while i >= 0:
        ct = 0
        c = nums[i]
        for j in range(i - 1, -1, -1):
            if (nums[j] < nums[i]):
                c -= nums[j]
                ct += 1
            else:
                break
        i -= ct
        fnums.append(c)
        i -= 1

    return sum(fnums)
