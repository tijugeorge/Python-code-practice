# implementing queue using 2 stacks

class QueueTwoStacks:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def enqueue(self, item):
        self.in_stack.append(item)

    def dequeue(self):
        if len(self.out_stack) == 0:
            while len(self.in_stack) > 0:
                newest_in_stack_item = self.in_stack.pop()
                self.out_stack.append(newest_in_stack_item)

            if len(self.out_stack) == 0:
                raise IndexError("Can't dequeue from empty queue!")
        return self.out_stack.pop()


list = [1, 2, 3, 4, 5, 6, 7, 8]
list2 = []
print list, list2
q = QueueTwoStacks()
for i in list:
    q.enqueue(i)
print 'This is instack filled up: ',q.in_stack
for i in range(len(list)):
    list2.append(q.dequeue())
print 'Here it goes, list 2 is filled up: ',list2
