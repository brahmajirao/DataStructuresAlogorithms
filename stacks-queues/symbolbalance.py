
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

def is_balanced_symbol(open_index, close_index):
    open_symbols = "([{"
    close_symbols = ")]}"
    return open_symbols.index(open_index) == close_symbols.index(close_index)

def balance_check(s):
    stack = Stack()
    is_balanced = 0
    lst_open_symbols = ["[", "(", "{"]
    for sym in s:
        if sym in lst_open_symbols:
            stack.push(sym)
            is_balanced = 0
        else:
            if stack.size() == 0:
                lst_inserted = stack.pop()
                if is_balanced_symbol(lst_inserted, sym):
                    is_balanced = 1
                else:
                    is_balanced = 0
            else:
                return 0
    return is_balanced


if __name__ == "__main__":
    print(balance_check('[](){([[[]]]))}'))