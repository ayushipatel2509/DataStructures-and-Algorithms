class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


def TraverseAndPrint(head):
    currentNode = head
    while currentNode:
        print(currentNode.data , end="->")
        currentNode = currentNode.next
    print("Null")

node1 = Node(3)
node2 = Node(5)
node3 = Node(1)
node4 = Node(14)
node5 = Node(7)    

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

TraverseAndPrint(node1)