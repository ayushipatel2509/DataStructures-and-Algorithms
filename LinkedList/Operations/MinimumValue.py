class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def minValue(head):
    minValue = head.data
    currentNode = head.next
    while currentNode:
        if currentNode.data < minValue:
            minValue = currentNode.data
        currentNode = currentNode.next
    return minValue

node1 = Node(3)
node2 = Node(5)
node3 = Node(10)
node4 = Node(14)
node5 = Node(7)    

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5     

print("The minimum value from the given Linked List is ", minValue(node1))