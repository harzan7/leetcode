
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


def main():
    # test 1
    test1_nums1 = [1, 3]
    test1_nums2 = [2]
    expected1 = 2.0
    actual1 = find_median_sorted_arrays_naive(test1_nums1, test1_nums2)
    print("Median of", test1_nums1, "+", test1_nums2, "->", actual1)
    assert actual1 == expected1

    # test 2
    test2_nums1 = [1, 2]
    test2_nums2 = [3, 4]
    expected2 = 2.5
    actual2 = find_median_sorted_arrays_naive(test2_nums1, test2_nums2)
    print("Median of", test2_nums1, "+", test2_nums2, "->", actual2)
    assert actual2 == expected2


if __name__ == '__main__':
    main()