

def two_sum_naive(nums, target):
    """
    Given an array of integers, return indices of the two numbers such that they add up to target.
    Naive solution to two-sum problem, involving nested for loops.
    O(n^2) time complexity.
    O(1) space complexity.
    :param nums: Array of integers.
    :param target: Target number.
    :return: Indices of the two numbers such that they add up to target.
    """
    length = len(nums)
    for i in range(length):
        for j in range(i + 1, length):
            if nums[i] + nums[j] == target:
                return [i, j]


def two_sum_two_hash(nums, target):
    """
    Given an array of integers, return indices of the two numbers such that they add up to target.
    Involves two passes with hashmaps.
    Faster solution than naive implementation.
    O(n) time complexity.
    O(n) space complexity.
    :param nums: Array of integers.
    :param target: Target number.
    :return: Indices of the two numbers such that they add up to target.
    """
    length = len(nums)
    nums_hash = {}

    for i in range(length):
        nums_hash[nums[i]] = i

    for i in range(length):
        complement = target - nums[i]
        if complement in nums_hash and nums_hash[complement] != i:
            return [i, nums_hash[complement]]

