from ArrayStack import ArrayStack


class MaxStack():
    def __init__(self):
        self.data = ArrayStack()
        self.maximum = None

    def is_empty(self):
        return self.data.is_empty()

    def __len__(self):
        return len(self.data)

    def push(self, e):
        self.data.push((e, self.maximum))
        if (self.maximum == None) or (e > self.maximum):
            self.maximum = e

    def top(self):
        if self.is_empty():
            raise Exception("Empty Stack")
        return self.data.top()[0]

    def pop(self):
        if self.is_empty():
            raise Exception("Empty Stack")
        top_item = self.data.pop()
        if (top_item[1] == None) or (top_item[0] > top_item[1]):
            self.maximum = top_item[1]
        return top_item[0]

    def max(self):
        if self.is_empty():
            raise Exception("Empty Stack")
        return self.maximum
