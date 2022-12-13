from ArrayStack import ArrayStack


class Queue:
    def __init__(self):
        self.stack1 = ArrayStack()
        self.stack2 = ArrayStack()

    def __len__(self):
        return len(self.stack1) + len(self.stack2)

    def is_empty(self):
        return len(self) == 0

    def first(self):
        if self.is_empty() is True:

            raise Exception("Empty Queue")
        return self.first_element

    def enqueue(self, val):
        self.stack1.push(val)

    def dequeue(self):
        if self.is_empty() is True:

            raise Exception("Empty Queue")

        if self.stack2.is_empty() is True:
            for i in range(0, len(self.stack1)):
                self.stack2.push(self.stack1.pop())

        return self.stack2.pop()

