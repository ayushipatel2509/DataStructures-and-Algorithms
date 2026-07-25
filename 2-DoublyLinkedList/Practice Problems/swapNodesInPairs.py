class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print(self):
        current = self.head
        while current is not None:
            print(current.value, end="->")
            current = current.next
        print("None")

    def append(self, value):
        new_node = Node(value)
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
        self.length += 1
        return True

    def swap_pairs(self):
        if self.head is None or self.head.next is None:
            return True

        dummy = Node(None)
        dummy.next = self.head
        self.head.prev = dummy
        prev_pair = dummy

        while prev_pair.next is not None and prev_pair.next.next is not None:
            first = prev_pair.next
            second = first.next
            third = second.next

            second.next = first
            second.prev = prev_pair
            first.next = third
            first.prev = second
            if third is not None:
                third.prev = first

            prev_pair.next = second
            prev_pair = first

        self.head = dummy.next
        self.head.prev = None

        # recompute tail
        current = self.head
        while current.next is not None:
            current = current.next
        self.tail = current

        return True


# ===================== FUNCTION CALLS =====================

list1 = DoublyLinkedList(1)
list1.append(2); list1.append(3); list1.append(4)
list1.print()                        # 1->2->3->4->None
list1.swap_pairs()
list1.print()                        # 2->1->4->3->None

list2 = DoublyLinkedList(1)
list2.append(2); list2.append(3)
list2.print()                        # 1->2->3->None
list2.swap_pairs()
list2.print()                        # 2->1->3->None (odd leftover untouched)