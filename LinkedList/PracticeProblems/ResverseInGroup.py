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

    # reverses one group of k nodes starting at `head`, then recursively
    # handles the rest of the list; returns the new head of this segment
    def reverse_k_group(self, head, k):
        node = head
        count = 0
        while node is not None and count < k:
            node = node.next
            count += 1
        if count < k:
            return head 
        temp = head
        before = None
        for _ in range(k):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

        head.next = self.reverse_k_group(temp, k)  # connect to the next group
        return before

    def reverse_in_groups(self, k):
        self.head = self.reverse_k_group(self.head, k)
        # tail may have moved, so walk to find it
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        self.tail = temp



my_list = LinkedList(1)
for v in [2, 3, 4, 5, 6, 7, 8]:
    my_list.append(v)

print("Before:")
my_list.print_list()

my_list.reverse_in_groups(3)

print("After reverse_in_groups(k=3):")
my_list.print_list()
print("Head:", my_list.head.value, "Tail:", my_list.tail.value, "Length:", my_list.length)