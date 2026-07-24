class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def add_two_numbers(l1, l2):
    dummy_result = ListNode(None)
    p = dummy_result
    p1 = l1
    p2 = l2
    carry = 0

    while p1 or p2 or carry:
        v1 = p1.val if p1 is not None else 0
        v2 = p2.val if p2 is not None else 0

        total = v1 + v2 + carry
        digit = total % 10
        carry = total // 10

        digit_node = ListNode(digit)
        p.next = digit_node
        p = p.next

        if p1 is not None:
            p1 = p1.next
        if p2 is not None:
            p2 = p2.next

    return dummy_result.next


# ---- helpers to build/print a linked list ----
def build_list(values):
    dummy = ListNode()
    p = dummy
    for v in values:
        p.next = ListNode(v)
        p = p.next
    return dummy.next


def print_list(node):
    vals = []
    while node:
        vals.append(str(node.val))
        node = node.next
    print(" -> ".join(vals))


# ---- function calling ----
l1 = build_list([2, 4, 3])   # represents 342
l2 = build_list([5, 6, 4])   # represents 465

result = add_two_numbers(l1, l2)
print_list(result)   # 7 -> 0 -> 8