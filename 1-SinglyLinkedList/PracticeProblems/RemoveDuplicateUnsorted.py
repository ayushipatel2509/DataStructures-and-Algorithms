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

    # O(n^2) time, O(1) space -- no set used
    def remove_duplicate_unsorted_no_set(self):
        if self.head is None:
            return None
        current = self.head
        while current is not None:
            runner = current.next
            pre = current
            while runner is not None:
                if runner.value == current.value:
                    pre.next = runner.next
                    runner.next = None
                    runner = pre.next
                else:
                    pre = runner
                    runner = runner.next
            current = current.next
        return True


# ---- demo ----
my_list = LinkedList(1)
for v in [2, 3, 1, 4, 2, 5]:
    my_list.append(v)

print("Before:")
my_list.print_list()

my_list.remove_duplicate_unsorted_no_set()

print("After:")
my_list.print_list()