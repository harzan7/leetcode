

def two_sum_naive(nums, target):
    """
    Given an array of integers, return indices of the two numbers such that they add up to target.
    Naive solution to two-sum problem, involving nested for loops.
    :param nums: Array of integers.
    :param target: Target number.
    :return: Indices of the two numbers such that they add up to target.
    """
    length = len(nums)
    for i in range(length):
        for j in range(i + 1, length):
            if nums[i] + nums[j] == target:
                return [i, j]