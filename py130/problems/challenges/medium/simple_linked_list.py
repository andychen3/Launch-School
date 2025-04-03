# https://launchschool.com/exercises/23cf413a

class Element:
    def __init__(self, datum=None, next=None):
        self.datum = datum
        self.next = next

    def is_tail(self):
        if self.next is None:
            return True
        return False


class SimpleLinkedList:
    def __init__(self):
        self.size = 0
        self.head = None

    def is_empty(self):
        return self.size == 0
    
    def push(self, num):
        if not self.head:
            self.head = Element(num)
        else:
            new_elem = Element(num)
            new_elem.next = self.head
            self.head = new_elem
        self.size += 1

    def peek(self):
        return self.head.datum if self.head else None
    
    def pop(self):
        new_head = self.head.next
        curr = self.head
        curr.next = None
        self.head = new_head
        self.size -= 1
        return curr.datum
    
    @classmethod
    def from_list(cls, lst):
        simple_ll = SimpleLinkedList()

        if not lst:
            return simple_ll

        for datum in reversed(lst):
            simple_ll.push(datum)
        return simple_ll

    def to_list(self):
        if self.size == 0:
            return []
        
        res = []
        curr = self.head
        while curr != None:
            res.append(curr.datum)
            curr = curr.next
        return res
    
    def reverse(self):
        ll = SimpleLinkedList()
        curr = self.head

        while curr != None:
            ll.push(curr.datum)
            curr = curr.next
        return ll

