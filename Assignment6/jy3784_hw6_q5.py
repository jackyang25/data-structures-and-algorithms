from DoublyLinkedList import DoublyLinkedList



def merge_linked_lists(srt_lnk_lst1, srt_lnk_lst2):
    ls1 = srt_lnk_lst1
    ls2 = srt_lnk_lst2

    def merge_sublists(cursor1, cursor2, ls1, ls2):
        if cursor1.data != None and cursor2.data == None:
            temp = DoublyLinkedList()
            while True:
                if cursor1.data == None:
                    break
                else:
                    temp.add_last(cursor1.data)
                    cursor1 = cursor1.next

        elif cursor1.data == None and cursor2.data != None:
            temp = DoublyLinkedList()
            while True:
                if cursor2.data == None:
                    break
                else:
                    temp.add_last(cursor2.data)
                    cursor2 = cursor2.next

        else:
            if cursor1.data <= cursor2.data:
                temp = merge_sublists(cursor1.next, cursor2, ls1, ls2)
                temp.add_first(cursor1.data)

            else:
                temp = merge_sublists(cursor1, cursor2.next, ls1, ls2)
                temp.add_first(cursor2.data)

        return temp

    return merge_sublists(ls1.header.next, ls2.header.next, ls1, ls2)