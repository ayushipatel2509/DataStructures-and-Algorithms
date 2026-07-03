class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

node1 = Node(4)
node2 = Node(12)
node3 = Node(7)
node4 = Node(3)

node1.prev = node4
node1.next = node2

node2.prev = node1
node2.next = node3

node3.prev = node2
node3.next = node4

node4.prev = node3
node4.next = node1

print("\nForward Traversal")
currentNode = node1
startNode = node1
print(currentNode.data, end = "->")
currentNode = currentNode.next
while currentNode != startNode:
    print(currentNode.data, end = "->")
    currentNode = currentNode.next
print("...")

print("\nBackward Traversal")
currentNode = node4
startNode = node4
print(currentNode.data, end = "->")
currentNode = currentNode.prev
while currentNode != startNode:
    print(currentNode.data, end = "->")
    currentNode = currentNode.prev
print("...")


        