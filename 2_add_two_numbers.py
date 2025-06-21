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
