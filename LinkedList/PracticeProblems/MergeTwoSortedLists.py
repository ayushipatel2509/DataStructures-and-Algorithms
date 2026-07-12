class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value, end=" -> " if temp.next else "\n")
            temp = temp.next

    # merges two sorted lists (given as raw head-node references)
    # and returns the head node of the merged, sorted list
    def merge_two_lists(self, list1, list2):
        dummy = Node(None)
        tail = dummy

        while list1 is not None and list2 is not None:
            if list1.value < list2.value:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        # attach whatever's left — already sorted, no more comparing needed
        if list1 is not None:
            tail.next = list1
        else:
            tail.next = list2

        return dummy.next


# ---- demo ----
list_a = LinkedList()
for v in [1, 3, 5]:
    list_a.append(v)

list_b = LinkedList()
for v in [2, 4, 6]:
    list_b.append(v)

print("List A:")
list_a.print_list()
print("List B:")
list_b.print_list()

merger = LinkedList()  # any LinkedList instance can call the method — self isn't used inside it
merged_head = merger.merge_two_lists(list_a.head, list_b.head)

# print the merged result by walking from merged_head directly
print("Merged:")
temp = merged_head
while temp is not None:
    print(temp.value, end=" -> " if temp.next else "\n")
    temp = temp.next