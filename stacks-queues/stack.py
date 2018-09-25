class Stack(object):
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peep(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


if __name__ == "__main__":
    stk = Stack()
    print(stk.is_empty())
    print(stk.peep())