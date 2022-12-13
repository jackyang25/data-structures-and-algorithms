# what:

# make a queue that uses the underlying data structure of a linkedlist

# all queue operations should use 0(1) worst-case



from DoublyLinkedList import DoublyLinkedList

class LinkedQueue:
    def __init__(self):
        self.ls = DoublyLinkedList()

    def __len__(self):
        return len(self.ls)

    def enqueue(self, item):
        self.ls.add_last(item)

    def dequeue(self):
        if(self.is_empty()):
            raise Exception("LinkedQueue is empty")
        else:
            return self.ls.delete_first()

    def is_empty(self):
        return (len(self) == 0)


    def first(self):
        if(self.is_empty()):
            raise Exception("Queue is empty")
        return self.ls.header.next.data



