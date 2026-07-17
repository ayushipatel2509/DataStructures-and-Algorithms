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

    def remove_nth_from_end(self, n):
        if n <= 0 or n > self.length:
            return False

        fast = self.head
        for _ in range(n):
            fast = fast.next

        # if fast fell off the list, n == length -> we're removing the head
        if fast is None:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            self.length -= 1
            if self.length == 0:
                self.tail = None
            return True

        slow = self.head
        while fast.next is not None:
            fast = fast.next
            slow = slow.next

        pre = slow
        temp = pre.next
        pre.next = temp.next
        if temp is self.tail:
            self.tail = pre
        temp.next = None
        self.length -= 1
        return True


# ---- demo ----
my_list = LinkedList(1)
for v in [2, 3, 4, 5]:
    my_list.append(v)

print("Before:")
my_list.print_list()

my_list.remove_nth_from_end(2)   # removes node 4 (2nd from end)
print("After removing 2nd from end:")
my_list.print_list()
print("Head:", my_list.head.value, "Tail:", my_list.tail.value, "Length:", my_list.length)

my_list.remove_nth_from_end(1)   # removes the tail (node 5)
print("After removing 1st from end (tail):")
my_list.print_list()
print("Head:", my_list.head.value, "Tail:", my_list.tail.value, "Length:", my_list.length)

my_list.remove_nth_from_end(3)   # length is 3 now -> removes the head (node 1)
print("After removing 3rd from end (head case):")
my_list.print_list()
print("Head:", my_list.head.value, "Tail:", my_list.tail.value, "Length:", my_list.length)