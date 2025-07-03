
def find_median_sorted_arrays_naive(nums1, nums2):
    """
    Naive solution to the median of two sorted arrays' problem.
    O((n+m)log(n+m)) time complexity.
    O(n+m) space complexity.
    :param nums1: First sorted array.
    :param nums2: Second sorted array.
    :return: Median of the merged sorted arrays.
    """
    merged_arr = nums1 + nums2
    merged_arr.sort()
    mid = len(merged_arr) // 2
    return merged_arr[mid] if len(merged_arr) % 2 == 1 else (merged_arr[mid] + merged_arr[mid - 1]) / 2


def find_median_sorted_arrays_optimal(nums1, nums2):
    """
    Optimal solution to the median of two sorted arrays' problem.
    O(log (min(n, m))) time complexity.
    O(1) space complexity.
    :param nums1: First sorted array.
    :param nums2: Second sorted array.
    :return: Median of the merged sorted arrays.
    """
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    m, n = len(nums1), len(nums2)
    left, right = 0, m

    while left <= right:
        partition1 = (left + right) // 2
        partition2 = (m + n + 1) // 2 - partition1

        max_left1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
        min_right1 = float('inf') if partition1 == m else nums1[partition1]

        max_left2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
        min_right2 = float('inf') if partition2 == n else nums2[partition2]

        if max_left1 <= min_right2 and max_left2 <= min_right1:
            if (m + n) % 2 == 0:
                return (max(max_left1, max_left2) + min(min_right1, min_right2)) / 2
            else:
                return max(max_left1, max_left2)
        elif max_left1 > min_right2:
            right = partition1 - 1
        else:
            left = partition1 + 1

    raise ValueError("Input arrays are not sorted or invalid.")


def main():
    # test 1
    test1_nums1 = [1, 3]
    test1_nums2 = [2]
    expected1 = 2.0
    actual1 = find_median_sorted_arrays_optimal(test1_nums1, test1_nums2)
    print("Median of", test1_nums1, "+", test1_nums2, "->", actual1)
    assert actual1 == expected1

    # test 2
    test2_nums1 = [1, 2]
    test2_nums2 = [3, 4]
    expected2 = 2.5
    actual2 = find_median_sorted_arrays_optimal(test2_nums1, test2_nums2)
    print("Median of", test2_nums1, "+", test2_nums2, "->", actual2)
    assert actual2 == expected2


if __name__ == '__main__':
    main()