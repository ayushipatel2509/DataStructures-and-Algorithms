class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node
        self.length += 1 
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next    
            
    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def partition_list(self, x):
        dummy1 = Node(0)
        dummy2 = Node(0)
        p1 = dummy1
        p2 = dummy2
        current = self.head
        while current is not None:
            if current.value < x:
                p1.next = current
                p1 = current
            else:
                p2.next = current
                p2 = current
            current = current.next
        p2.next = None
        p1.next = dummy2.next
        self.head = dummy1.next


#  +=====================================================+
#  |                                                     |
#  |          THE TEST CODE BELOW WILL PRINT             |
#  |              OUTPUT TO "USER LOGS"                  |
#  |                                                     |
#  |  Use the output to test and troubleshoot your code  |
#  |                                                     |
#  +=====================================================+


def linkedlist_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.value)
        current = current.next
    return result

def test_partition_list():
    test_cases_passed = 0

    print("-----------------------")
    print("Test 1: Partition in Middle")
    x = 5
    print(f"x = {x}")
    ll = LinkedList(5)
    for i in [8, 3, 10, 2, 4]:
        ll.append(i)
    print("Before:", linkedlist_to_list(ll.head))
    ll.partition_list(x)
    print("After:", linkedlist_to_list(ll.head))
    if linkedlist_to_list(ll.head) == [3, 2, 4, 5, 8, 10]:
        print("PASS"); test_cases_passed += 1
    else:
        print("FAIL")

    print("-----------------------")
    print("Test 2: Partition at Start")
    x = 3
    print(f"x = {x}")
    ll = LinkedList(5)
    for i in [8, 3, 10, 2, 4]:
        ll.append(i)
    print("Before:", linkedlist_to_list(ll.head))
    ll.partition_list(x)
    print("After:", linkedlist_to_list(ll.head))
    if linkedlist_to_list(ll.head) == [2, 5, 8, 3, 10, 4]:
        print("PASS"); test_cases_passed += 1
    else:
        print("FAIL")

    print("-----------------------")
    print("Test 3: Partition at End")
    x = 11
    print(f"x = {x}")
    ll = LinkedList(5)
    for i in [8, 3, 10, 2, 4]:
        ll.append(i)
    print("Before:", linkedlist_to_list(ll.head))
    ll.partition_list(x)
    print("After:", linkedlist_to_list(ll.head))
    if linkedlist_to_list(ll.head) == [5, 8, 3, 10, 2, 4]:
        print("PASS"); test_cases_passed += 1
    else:
        print("FAIL")

    print("-----------------------")
    print("Test 4: Empty List")
    x = 5
    print(f"x = {x}")
    ll = LinkedList(1)
    ll.make_empty()
    print("Before:", linkedlist_to_list(ll.head))
    ll.partition_list(x)
    print("After:", linkedlist_to_list(ll.head))
    if ll.head is None:
        print("PASS"); test_cases_passed += 1
    else:
        print("FAIL")

    print("-----------------------")
    print("Test 5: All Greater or Equal")
    x = 3
    print(f"x = {x}")
    ll = LinkedList(5)
    for i in [6, 7, 8]:
        ll.append(i)
    print("Before:", linkedlist_to_list(ll.head))
    ll.partition_list(x)
    print("After:", linkedlist_to_list(ll.head))
    if linkedlist_to_list(ll.head) == [5, 6, 7, 8]:
        print("PASS"); test_cases_passed += 1
    else:
        print("FAIL")

    print("-----------------------")
    print("Test 6: Single Element")
    x = 5
    print(f"x = {x}")
    ll = LinkedList(4)
    print("Before:", linkedlist_to_list(ll.head))
    ll.partition_list(x)
    print("After:", linkedlist_to_list(ll.head))
    if linkedlist_to_list(ll.head) == [4]:
        print("PASS"); test_cases_passed += 1
    else:
        print("FAIL")

    print("-----------------------")
    print("Test 7: Duplicates Equal to x")
    x = 3
    print(f"x = {x}")
    ll = LinkedList(3)
    for i in [1, 3, 2, 3]:
        ll.append(i)
    print("Before:", linkedlist_to_list(ll.head))
    ll.partition_list(x)
    print("After:", linkedlist_to_list(ll.head))
    if linkedlist_to_list(ll.head) == [1, 2, 3, 3, 3]:
        print("PASS"); test_cases_passed += 1
    else:
        print("FAIL")

    print("-----------------------")
    print("Test 8: Already Partitioned")
    x = 5
    print(f"x = {x}")
    ll = LinkedList(1)
    for i in [2, 5, 8, 10]:
        ll.append(i)
    print("Before:", linkedlist_to_list(ll.head))
    ll.partition_list(x)
    print("After:", linkedlist_to_list(ll.head))
    if linkedlist_to_list(ll.head) == [1, 2, 5, 8, 10]:
        print("PASS"); test_cases_passed += 1
    else:
        print("FAIL")

    print("-----------------------")
    print(f"{test_cases_passed} out of 8 tests passed.")

test_partition_list()