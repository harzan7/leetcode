

def longest_palindrome_naive(s):
    """
    Naive solution to the longest palindromic substring problem.
    O(n^3) time complexity.
    O(n) space complexity.
    :param s: Given string.
    :return: Longest palindromic substring.
    """
    max_len = 0
    max_pal = ""

    for i in range(len(s)):
        for j in range(i, len(s)):
            pal = s[i:j+1]
            if pal == pal[::-1] and len(pal) > max_len:
                max_pal = pal
                max_len = len(pal)

    return max_pal


def longest_palindrome_optimal(s):
    """
    Optimal solution to the longest palindromic substring problem.
    Expand around the center of the string.
    O(n^2) time complexity.
    O(1) space complexity.
    :param s: Given string.
    :return: Longest palindromic substring.
    """
    # Edge case: empty string
    if not s:
        return ""

    # Initialize start and end indices of the longest palindrome found
    start, end = 0, 0

    # Helper function to expand around the center and find the longest palindrome
    def expand_around_center(left, right):
        # Keep expanding outwards while characters match and within bounds
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1   # Move left pointer backward
            right += 1  # Move right pointer forward

        # Return the length of the palindrome found
        # (right - left - 1) because the loop overshoots by 1
        return right - left - 1

    # Iterate through each character in the string
    for i in range(len(s)):
        # Case 1: Odd-length palindrome (center is a single character)
        len1 = expand_around_center(i, i)
        # Case 2: Even-length palindrome (center is between two characters)
        len2 = expand_around_center(i, i+1)
        # Get the maximum length between the two cases
        max_len = max(len1, len2)

        # If the current palindrome is longer than the previous longest
        if max_len > end-start:
            # Update start and end indices
            # For odd-length: center is i
            # For even-length: center is between i and i+1
            start = i - (max_len - 1) // 2
            end = i + max_len // 2

    # Return the longest palindrome substring
    return s[start:end+1]


def main():
    # test 1
    s1 = "babad"
    expected1 = "bab"
    expected1_1 = "aba"
    actual1 = longest_palindrome_optimal(s1)
    print("Longest palindrome in", s1, "->", actual1)
    assert actual1 == expected1 or actual1 == expected1_1

    # test 2
    s2 = "cbbd"
    expected2 = "bb"
    actual2 = longest_palindrome_optimal(s2)
    print("Longest palindrome in", s2, "->", actual2)
    assert actual2 == expected2


if __name__ == '__main__':
    main()

