
def length_of_longest_substring_naive(s):
    """
    Naive solution to the longest substring without repeating characters' problem.
    O(n^2) time complexity.
    O(min(n, m)) space complexity, where m is the number of unique characters in s.
    :param s: Given string.
    :return: Length of the longest substring without repeating characters.
    """
    unique_chars = set()
    lengths = set()

    for i in range(len(s)):
        cur_len = 0
        j = i

        while j < len(s) and s[j] not in unique_chars:
            cur_len += 1
            unique_chars.add(s[j])
            j += 1

        lengths.add(cur_len)
        unique_chars.clear()

    return max(lengths)


def length_of_longest_substring_optimal(s):
    """
    Optimal solution to the longest substring without repeating characters' problem.
    O(n) time complexity.
    O(min(n, m)) space complexity, where m is the number of unique characters in s.
    :param s: Given string.
    :return: Length of the longest substring without repeating characters.
    """
    char_set = set()    # unique chars
    left = 0
    max_len = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1

        char_set.add(s[right])
        max_len = max(max_len, right - left + 1)

    return max_len


def main():
    # Tests
    s1 = "abcabcbb"
    expected1 = 3
    actual1 = length_of_longest_substring_optimal(s1)
    print("Length of longest substring in", s1, "->", actual1)
    assert actual1 == expected1

    s2 = "bbbbb"
    expected2 = 1
    actual2 = length_of_longest_substring_optimal(s2)
    print("Length of longest substring in", s2, "->", actual2)
    assert actual2 == expected2

    s3 = "pwwkew"
    expected3 = 3
    actual3 = length_of_longest_substring_optimal(s3)
    print("Length of longest substring in", s3, "->", actual3)
    assert actual3 == expected3


if __name__ == '__main__':
    main()