from SLNode import SLNode

class Slist:
    def __init__(self):
        self.head = None

    def add_to_front(self, val):
        newNode = SLNode(val)
        current = self.head
        newNode.next = current
        self.head = newNode
        return self

    def add_to_back(self, val):
        newNode = SLNode(val)
        if self.head == None:
            self.head = newNode
            return self

        runner = self.head
        while (runner.next != None):
            runner = runner.next
        runner.next = newNode
        return self

    def print_values(self):
        runner = self.head
        while (runner != None):
            print(runner.value, "->")
            runner = runner.next
        print(None)
        return self

    def remove_from_front(self):
        if self.head == None:
            return None
        else:
            removed = self.head.value
            self.head = self.head.next
        return removed

    def remove_from_back(self):
        if self.head == None:
            return None
        elif self.head.next == None:
            removed = self.head.value
            self.head = None
            return removed
        else:
            prev = None
            current = self.head
            while current.next != None:
                prev = current
                current = current.next
            removed = current.value
            prev.next = None
            return removed

    def remove_val(self, val):
        if self.head == None:
            return None
        prev = None
        current = self.head
        while current != None and current.value != val:
            prev = current
            current = current.next
        if current == None:
            return None
        if prev == None:
            self.head = current.next
            removed = current.value
            return removed
        else:
            removed = current.value
            prev.next = current.next
            return removed

    def insert_at(self, val, n):
        newNode = SLNode(val)

        if n == 0:
            newNode.next = self.head
            self.head = newNode
            return self

        current = self.head
        x = 0
        while current != None and x != n-1:
            current = current.next
            x = x + 1

        if current == None:
            return None

        newNode.next = current.next
        current.next = newNode
        return self

myList = Slist()
myList.add_to_back(10)
myList.add_to_back(20)
myList.add_to_back(30)

myList.insert_at(99, 0)
myList.insert_at(55, 2)
myList.insert_at(77, 5)
myList.insert_at(11, 20)
myList.print_values()