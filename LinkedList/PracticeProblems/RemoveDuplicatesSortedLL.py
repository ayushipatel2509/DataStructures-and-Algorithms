class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1
        return True

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value, end=" -> " if temp.next else "\n")
            temp = temp.next

    # SORTED linked list only — duplicates are guaranteed adjacent
    def remove_duplicates_sortedll(self):
        if self.head is None:
            return None
        p1 = self.head
        p2 = p1.next
        while p2 is not None:
            if p1.value == p2.value:
                temp = p2
                pre = p1
                pre.next = temp.next
                temp.next = None
                p2 = pre.next
            else:
                p1 = p1.next
                p2 = p2.next
        return True


# ---- demo ----
my_list = LinkedList(1)
for v in [1, 1, 2, 3, 3, 3, 4, 5, 5]:
    my_list.append(v)

print("Before:")
my_list.print_list()

my_list.remove_duplicates_sortedll()

print("After remove_duplicates_sortedll():")
my_list.print_list()