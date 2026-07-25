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

    def merge_sorted_lists(self, headA, headB):
        dummy = Node(None)
        tail = dummy

        while headA and headB:
            if headA.value < headB.value:
                tail.next = headA
                headA.prev = tail
                headA = headA.next
            else:
                tail.next = headB
                headB.prev = tail
                headB = headB.next
            tail = tail.next

        if headA is None and headB is not None:
            tail.next = headB
            headB.prev = tail
        if headB is None and headA is not None:
            tail.next = headA
            headA.prev = tail

        return dummy.next


# ===================== FUNCTION CALLS =====================

listA = DoublyLinkedList(1)
listA.append(3)
listA.append(5)
listA.print()                       # 1->3->5->None

listB = DoublyLinkedList(2)
listB.append(4)
listB.append(6)
listB.print()                       # 2->4->6->None

merger = DoublyLinkedList.__new__(DoublyLinkedList)   # dummy instance just to call the method
merged_head = merger.merge_sorted_lists(listA.head, listB.head)

# print merged result forward via .next
current = merged_head
while current is not None:
    print(current.value, end="->")
    current = current.next
print("None")                       # 1->2->3->4->5->6->None

# verify .prev links are correct by walking backward from the last node
current = merged_head
while current.next is not None:
    current = current.next
while current is not None:
    print(current.value, end="->")
    current = current.prev
print("None")                       # 6->5->4->3->2->1->None