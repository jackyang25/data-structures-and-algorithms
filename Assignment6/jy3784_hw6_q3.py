from DoublyLinkedList import DoublyLinkedList


class CompactString:
    def __init__(self, orig_str):
        """ Initializes a CompactString object
        representing the string given in orig_str"""
        occur = 1
        self.ls = DoublyLinkedList()


        for j in range(1, len(orig_str)):
            curr = orig_str[j]
            pre = orig_str[j - 1]
            if curr == pre:
                occur = occur + 1

            if curr != pre:
                self.ls.add_last((curr, occur))
                occur = 1

        lens = len(orig_str)
        if lens != 0:
            self.ls.add_last((orig_str[len(orig_str) - 1], occur))

    def __add__(self, other):
        str = CompactString("")
        cursor = self.ls.header.next
        while True:
            if cursor.next.data == None:
                break
            else:

                str.ls.add_last(cursor.data)
                cursor = cursor.next

        if cursor.data[0] is other.ls.header.next.data[0]:
            str.ls.add_last((cursor.data[0], cursor.data[1] + other.ls.header.next.data[1]))
            cursor = other.ls.header.next.next
        else:
            str.data.add_last(cursor.data)
            cursor = other.ls.header.next

        while True:
            if cursor.data is None:
                break
            else:
                str.ls.add_last(cursor.data)
                cursor = cursor.next
        return str



    def __repr__(self):
        """ Creates and returns the string representation
        (of type str) of self"""
        cursor = self.ls.header.next
        string = ""
        while True:
            if cursor == self.ls.trailer:
                break
            else:
                string += cursor.data[0] * cursor.data[1]
                cursor = cursor.next

        return string


