from DoublyLinkedList import DoublyLinkedList

class Integer:
    def __init__(self, num_str):

        temp = [elem for elem in num_str]

        self.ls = DoublyLinkedList()

        for elem in temp:
            self.ls.add_last(int(elem))


    def __add__(self, other):
        """ Creates and returns an Integer object that
        represent the sum of self and other, also of
        type Integer"""

        cursor1 = other.ls.trailer.prev
        cursor2 = self.ls.trailer.prev
        num_carry = 0
        new = Integer("")

        while cursor1 != other.ls.header and cursor2 != self.ls.header:
            total = cursor1.data + cursor2.data + num_carry
            num_carry = total // 10
            remainder = total % 10
            new.ls.add_first(remainder)
            cursor1 = cursor1.prev
            cursor2 = cursor2.prev

        if cursor1 == other.ls.header:
            new_cursor = cursor2
        else:
            new_cursor = cursor1

        while new_cursor.data is not None:
            total = new_cursor.data + num_carry
            num_carry = total // 10
            remainder = total % 10
            new.ls.add_first(remainder)
            new_cursor = new_cursor.prev

        if num_carry > 0:
            new.ls.add_first(num_carry)

        temp = new.ls

        while temp.header.next.data == 0:
            temp.delete_first()

        new.ls = temp

        return new



    def __repr__(self):
            """ Creates and returns the string representation
            of self"""
            temp = []

            head = self.ls.header.next
            while head is not self.ls.trailer:
                temp.append(str(head.data))
                head = head.next

            return "".join(temp)


# n4 = Integer('007')
# n5 = Integer('20')
# n6 = n4 + n5
# print(n6)
