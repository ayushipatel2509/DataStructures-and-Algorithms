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

    def remove_duplicates_unsortedll(self):
        if self.head is None:
            return None
        seen = set()
        pre = self.head
        seen.add(pre.value)
        current = pre.next
        while current is not None:
            if current.value in seen:
                pre.next = current.next
                current.next = None
                current = pre.next
            else:
                seen.add(current.value)
                pre = current
                current = current.next
        return True


# ---- demo ----
my_list = LinkedList(1)
for v in [2, 3, 1, 4, 2, 5]:
    my_list.append(v)

print("Before:")
my_list.print_list()

my_list.remove_duplicates_unsortedll()

print("After:")
my_list.print_list()