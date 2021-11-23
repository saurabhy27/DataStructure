class SLinkedList:
    def __init__(self):
        self.head = None

    def print_ll(self):  # complexity O(n)
        tmp = self.head
        if tmp is None:
            print("Empty Linked List.")
        while tmp:
            print("data {} ".format(tmp.data))
            tmp = tmp.next


    def insert_at_start(self, node6):  # complexity O(1)
        tmp = self.head
        self.head = node6
        node6.next = tmp

    def insert_at_loc(self, loc, node7):  # complexity O(n)
        tmp = self.head
        i = 0
        while tmp:
            if i == loc - 1:
                node7.next = tmp.next
                tmp.next = node7
            tmp = tmp.next
            i += 1

    def insert_at_end(self, node8):  # complexity O(n)
        tmp = self.head
        if tmp is None:
            self.head = node8
            return
        last = self.head
        while last:
            if last.next is None:
                break
            last = last.next
        last.next = node8

    def delete(self, node7):
        tmp = self.head
        if tmp is None:
            print("No data found in linkedList")
            return
        if tmp == node7:
            self.head = node7.next
            return
        prev = self.head
        while prev:
            if prev.next == node7:
                break
            prev = prev.next
        if prev is not None:
            prev.next = node7.next
            del node7
        else:
            print("Node not found")

    def delete_loc(self, loc):
        tmp = self.head
        if tmp is None:
            print("Empty Linked List.")
            return
        if loc == 0:
            self.head = tmp.next
            tmp = None
            return
        i = 0
        prev = self.head
        while prev:
            if i == loc - 1:
                break
            prev = prev.next
            i += 1
        if prev is not None and prev.next is not None:
            prev.next = prev.next.next
        else:
            print("data not found.")

    def delete_linked_list(self):
        tmp = self.head
        while tmp:
            prev = tmp.next
            del tmp
            tmp = prev
        self.head = None

    def length(self):
        tmp = self.head
        length = 0
        while tmp:
            length += 1
            tmp = tmp.next
        return length

    def search(self, node):
        tmp = self.head
        pres = False
        while tmp:
            if tmp == node:
                pres = True
                break
            tmp = tmp.next
        return pres

    def GetNth(self, loc):
        tmp = self.head
        i = 0
        while tmp:
            if i == loc:
                return tmp.data
            tmp = tmp.next
            i += 1
        return "No Data Found"

    def reverse(self):
        curr = self.head
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        self.head = prev

