def reverse_between_start_end(self,start,end):
    pre = self.get(start-1)
    original_start = self.get(start)
    current = original_start
    count = end - start +1

    for _ in range(count):
        temp = current.next
        current.next = current.prev
        current.prev = temp
        new_first = current
        current = current.prev

    pre.next = new_first
    new_first.prev = pre
    original_start.next = current
    current.prev = original_start