class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList:
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
        self.tail = new_node
        self.length += 1
        return True

    def swap_pairs_recursive(self, head):
        if head is None or head.next is None:
            return head
        first = head
        second = head.next
        third = second.next
        second.next = first
        first.next = self.swap_pairs_recursive(third)
        return second


# ===================== FUNCTION CALLS =====================

my_list = SinglyLinkedList(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.print()                                          # 1->2->3->4->None

my_list.head = my_list.swap_pairs_recursive(my_list.head)
my_list.print()                                           # 2->1->4->3->None