class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

node1 = Node(5)
node2 = Node(4)
node3 = Node(12)
node4 = Node(7)

node1.next = node2

node2.next = node3
node2.prev = node1

node3.next = node4
node3.prev = node2

node4.prev = node3

print("Travesing Forward")
currentNode = node1
while currentNode:
    print(currentNode.data , end="->")
    currentNode = currentNode.next
print("Null")

print("Traversing Backward")
currentNode = node4
while currentNode:
    print(currentNode.data , end="->")
    currentNode = currentNode.prev
print("Null")
