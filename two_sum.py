"""
https://leetcode.com/problems/two-sum/
"""


# Solution 1: O(n^2)
# We take each number in the list individually (x), and then we iterate again the list, starting from that number, until
# we find the number (y) that adds to the target number.
def twoSum(nums: list[int], target: int) -> list[int]:
    for x in range(len(nums)):
        for y in range(x + 1, len(nums)):
            if nums[x] + nums[y] == target:
                return [x, y]


# Solution 2: O(n)
# We iterate through the list and for each number we store in a hash table a key with the difference
# between the target and the number, and the value as the index, if that value does not exist. For each iteration we
# check for the number in dictionary and if found we return current number index and index from hash table.
def twoSum(nums: list[int], target: int) -> list[int]:
    cache = {}
    for idx, num in enumerate(nums):
        if num not in cache:
            cache[target - num] = idx
        else:
            return [cache[num], idx]
