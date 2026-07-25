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

    def remove_duplicates_unsorted_ll(self):
        seen = set()
        current = self.head
        while current is not None:
            next_node = current.next
            if current.value in seen:
                before = current.prev
                after = current.next

                before.next = after
                if after is not None:
                    after.prev = before
                else:
                    self.tail = before

                current.prev = None
                current.next = None
            else:
                seen.add(current.value)

            current = next_node


# ===================== FUNCTION CALLS =====================

list1 = DoublyLinkedList(4)
list1.append(2)
list1.append(4)
list1.append(1)
list1.append(2)
list1.append(3)
list1.print()                      # 4->2->4->1->2->3->None
list1.remove_duplicates_unsorted_ll()
list1.print()                      # 4->2->1->3->None

list2 = DoublyLinkedList(4)
list2.append(2)
list2.append(4)
list2.print()                      # 4->2->4->None
list2.remove_duplicates_unsorted_ll()
list2.print()                      # 4->2->None
print("tail after removal:", list2.tail.value)   # 2