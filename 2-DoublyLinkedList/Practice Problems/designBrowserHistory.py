class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
    
class BrowserHistory:
    def __init__(self,url):
        new_node = Node(url)
        self.head = new_node
        self.tail = new_node
        self.current = new_node

    def visit(self,url):
        new_node = Node(url)
        self.current.next = new_node
        new_node.prev = self.current
        self.current = self.current.next
        self.tail = self.current
    
    def back(self,steps):
        count = 0
        while self.current.prev is not None and count < steps:
            self.current = self.current.prev
            count += 1
        return self.current.value
    
    def forward(self,steps):
        count = 0
        while self.current.next is not None and count < steps:
            self.current = self.current.next
            count += 1
        return self.current.value
    

browser_history = BrowserHistory("google.com")
browser_history.visit("amazon.com")
browser_history.visit("apple.com")
print(browser_history.back(1))
print(browser_history.back(2))
browser_history.visit("netfix.com")
print(browser_history.back(2))
print(browser_history.forward(1))





        