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
            
    def get_intersection_point(self,headA, headB):
        p1 = headA
        p2 = headB
        while p1 is not p2:
            if p1 is None:
                p1 = headB
            else:
                p1 = p1.next

            if p2 is None:
                p2 = headA
            else:
                p2 = p2.next
        
        return p1
    
shared = LinkedList(7)
shared.append(8)
shared.append(9)

listA = LinkedList(1)
listA.append(2)
listA.append(3)
listA.tail.next = shared.head   # 1 -> 2 -> 3 -> 7 -> 8 -> 9

listB = LinkedList(5)
listB.append(6)
listB.tail.next = shared.head   # 5 -> 6 -> 7 -> 8 -> 9

print("List A:")
listA.print_list()   # note: will print 1->2->3->7->8->9->None-loop-safe since shared list ends at 9
print("List B:")
listB.print_list()

helper = LinkedList(0)  # any instance can call this method — it doesn't use self's own list
result = helper.get_intersection_point(listA.head, listB.head)
print("Intersection node value:", result.value if result else None)

# ---- no-intersection case, to prove it terminates correctly ----
listC = LinkedList(100)
listC.append(200)
listD = LinkedList(300)
result2 = helper.get_intersection_point(listC.head, listD.head)
print("No-intersection case result:", result2)