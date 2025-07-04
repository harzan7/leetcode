

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


def main():
    # test 1
    s1 = "babad"
    expected1 = "bab"
    actual1 = longest_palindrome_naive(s1)
    print("Longest palindrome in", s1, "->", actual1)
    assert actual1 == expected1

    # test 2
    s2 = "cbbd"
    expected2 = "bb"
    actual2 = longest_palindrome_naive(s2)
    print("Longest palindrome in", s2, "->", actual2)
    assert actual2 == expected2


if __name__ == '__main__':
    main()

