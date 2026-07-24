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

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        current = self.head
        for _ in range(index):
            current = current.next
        return current

    def reverse_between_startindex_endindex(self, start, end):
        temp = self.get(start)
        original_start = temp
        before = None
        count = end - start + 1

        for _ in range(count):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

        original_start.next = temp

        if start == 0:
            self.head = before
        else:
            pre_start = self.get(start - 1)
            pre_start.next = before

        return True


# ===================== FUNCTION CALLS =====================

my_list = SinglyLinkedList(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.append(5)
my_list.append(6)
my_list.print()                                       # 1->2->3->4->5->6->None

my_list.reverse_between_startindex_endindex(1, 3)
my_list.print()                                       # 1->4->3->2->5->6->None

# test start = 0 edge case on a fresh list
edge_list = SinglyLinkedList(1)
edge_list.append(2)
edge_list.append(3)
edge_list.append(4)
edge_list.print()                                     # 1->2->3->4->None

edge_list.reverse_between_startindex_endindex(0, 2)
edge_list.print()                                     # 3->2->1->4->None