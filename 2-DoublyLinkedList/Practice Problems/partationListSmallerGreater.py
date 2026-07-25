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

    def partition_list_smaller_greater(self, x):
        smaller_dummy = Node(None)
        greater_dummy = Node(None)
        p1 = smaller_dummy
        p2 = greater_dummy

        current = self.head
        while current:
            if current.value < x:
                p1.next = current
                current.prev = p1
                p1 = p1.next
            else:
                p2.next = current
                current.prev = p2
                p2 = p2.next
            current = current.next

        # stitch: smaller chain's tail connects to greater chain's head
        p1.next = greater_dummy.next
        if greater_dummy.next is not None:
            greater_dummy.next.prev = p1

        # set self.head — handle case where "smaller" group is empty
        if smaller_dummy.next is not None:
            self.head = smaller_dummy.next
        else:
            self.head = greater_dummy.next

        # set self.tail — handle case where "greater" group is empty
        if greater_dummy.next is not None:
            self.tail = p2
        else:
            self.tail = p1

        self.tail.next = None
        return True


# ===================== FUNCTION CALLS =====================

# Case 1: normal mixed case
list1 = DoublyLinkedList(1)
list1.append(4)
list1.append(3)
list1.append(2)
list1.append(5)
list1.append(2)
list1.print()                          # 1->4->3->2->5->2->None
list1.partition_list_smaller_greater(3)
list1.print()                          # 1->2->2->4->3->5->None
print("head:", list1.head.value, "tail:", list1.tail.value)

# Case 2: everything is "greater" (nothing smaller than x)
list2 = DoublyLinkedList(5)
list2.append(6)
list2.append(7)
list2.print()                          # 5->6->7->None
list2.partition_list_smaller_greater(3)
list2.print()                          # 5->6->7->None (unchanged, all "greater")
print("head:", list2.head.value, "tail:", list2.tail.value)

# Case 3: everything is "smaller" (nothing >= x)
list3 = DoublyLinkedList(1)
list3.append(2)
list3.append(0)
list3.print()                          # 1->2->0->None
list3.partition_list_smaller_greater(10)
list3.print()                          # 1->2->0->None (unchanged, all "smaller")
print("head:", list3.head.value, "tail:", list3.tail.value)

# Verify backward traversal on case 1
current = list1.tail
while current is not None:
    print(current.value, end="->")
    current = current.prev
print("None")                          # should read 5->3->4->2->2->1->None