class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def add_two_numbers(l1, l2):
    result_list = ListNode()
    cur_node = result_list
    carry_num = 0

    while l1 or l2:
        l1_val = l1.val if l1 else 0
        l2_val = l2.val if l2 else 0

        sum_vals = (l1_val + l2_val + carry_num) % 10
        carry_num = (l1_val + l2_val + carry_num) // 10

        cur_node.val = sum_vals

        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

        if l1 or l2:
            cur_node.next = ListNode()
            cur_node = cur_node.next

    if carry_num != 0:
        cur_node.val = carry_num

    return result_list


def linked_list_equality_checker(actual, expected):
    while actual or expected:
        if actual and expected:
            return False

        actual_val = actual.val
        expected_val = expected.val

        if actual_val != expected_val:
            return False

        actual = actual.next
        expected = expected.next

    return True


def main():
    l1 = ListNode(val=2, next=ListNode(4, next=ListNode(3, next=None)))
    l2 = ListNode(val=5, next=ListNode(val=6, next=ListNode(val=4, next=None)))
    expected = ListNode(val=7, next=ListNode(val=0, next=ListNode(val=8, next=None)))

    actual = add_two_numbers(l1, l2)

    result = linked_list_equality_checker(actual, expected)
    print(result)


if __name__ == '__main__':
    main()