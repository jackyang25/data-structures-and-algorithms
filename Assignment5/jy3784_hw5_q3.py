from ArrayStack import ArrayStack
from ArrayDeque import ArrayDeque

class MidStack:
    def __init__(self):
        self.Array_Top = ArrayDeque()
        self.Array_bottom = ArrayStack()

    def __len__(self):
        return len(self.Array_Top) + len(self.Array_bottom)

    def is_empty(self):
        is_empty = self.Array_Top.is_empty() and self.Array_bottom.is_empty()
        return is_empty

    def push(self, val):
        if len(self) % 2 == 1:
            last_elem = self.Array_Top.last()
            self.Array_bottom.push(last_elem)
            self.Array_Top.dequeue_last()
        self.Array_Top.enqueue_first(val)


    def mid_push(self, val):
        if (len(self) % 2 == 0):
            self.Array_Top.enqueue_last(val)
        else:
            temp_val = self.Array_Top.last()
            self.Array_Top.dequeue_last()
            self.Array_Top.enqueue_last(val)
            self.Array_bottom.push(temp_val)

    def top(self):
        if self.is_empty() is True:
            raise Exception("Empty MidStack")
        return self.Array_Top.first()


    def pop(self):
        if self.is_empty() is True:
            raise Exception("Empty MidStack")
        else:
            if len(self) % 2 == 0:
                top_elem = self.Array_bottom.pop()
                self.Array_Top.enqueue_last(top_elem)
            return self.Array_Top.dequeue_first()
