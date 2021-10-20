# How many even digits?
# Given an array of integers, return how many of them contain an even number of digits.
# Example 1:
# Input: nums = [12,345,2,6,7896]
# Output: 2
# Explanation:
# 12 contains 2 digits (even number of digits).
# 345 contains 3 digits (odd number of digits).
# 2 contains 1 digit (odd number of digits).
# 6 contains 1 digit (odd number of digits).
# 7896 contains 4 digits (even number of digits).
# Therefore only 12 and 7896 contain an even number of digits.
# Example 2:
# Input: nums = [555,901,482,1771]
# Output: 1
# Explanation:
# Only 1771 contains an even number of digits.

def even_nums(arr):
    res = 0
    for a in arr:
        if len(str(a)) % 2 == 0:
            res += 1
    return res

print(even_nums([12,345,2,6,7896]))
print(even_nums([1, 23, 234, 123, 34, 4567, 34]))
print(even_nums([23, 123, 3465, 3456, 43, 234, 1, 4565]))
        
