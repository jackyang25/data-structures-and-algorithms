import ArrayStack, ArrayQueue

def permutations(lst):
    final = []
    current = 0
    new = 0
    perm = ArrayQueue.ArrayQueue()
    left = ArrayStack.ArrayStack()

    for elem in lst:
        left.push(elem)
    if current == 0:
        
        temp = [left.pop()]
        perm.enqueue(temp)
        current = current + 1

    for i in range(0, len(left)):
        x = left.pop()

        for temp in range(0, current):
            current = perm.dequeue()
            for j in range(0, len(current) + 1):

                temp2 = list(current)
                temp2.insert(j, x)
                perm.enqueue(temp2)
                new = new + 1
        current = new

    while not perm.is_empty():
        final.append(perm.dequeue())

    else:
        return final


