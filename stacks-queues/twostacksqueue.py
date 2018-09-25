class Queue(object):
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, item):
        self.stack1.append(item)
        self.stack2 = [x for x in reversed(self.stack1)]

    def dequeue(self):
        #print(self.stack2)
        item = self.stack2.pop()
        self.stack1 = [x for x in reversed(self.stack2)]
        return item

    def isempty(self):
        return len(self.stack1) == 0


class Queue2Stacks(object):
    def __init__(self):

        # Two Stacks
        self.instack = []
        self.outstack = []

    def enqueue(self, element):

        # Add an enqueue with the "IN" stack
        self.instack.append(element)

    def dequeue(self):
        if not self.outstack:
            while self.instack:
                # Add the elements to the outstack to reverse the order when called
                self.outstack.append(self.instack.pop())
        return self.outstack.pop()

if __name__ == "__main__":
    q = Queue2Stacks()

    q.enqueue(0)
    q.enqueue(1)
    print(q.dequeue())
    q.enqueue(2)
    q.enqueue(3)
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())