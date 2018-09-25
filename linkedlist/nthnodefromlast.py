class Node(object):
    def __init__(self, value):
        self.value = value
        self.next_node = None

def nth_node_from_last(n, head):
    left_pointer = head
    right_pointer = head

    for i in range(n-1):
        if right_pointer.next_node is None:
            raise LookupError('n is larger than linkedlist')
        right_pointer = right_pointer.next_node

    while right_pointer.next_node:
        left_pointer = left_pointer.next_node
        right_pointer = right_pointer.next_node

    return left_pointer

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.next_node = b
b.next_node = c
c.next_node = d
d.next_node = e

# This would return the node d with a value of 4, because its the 2nd to last node.
target_node = nth_node_from_last(2, a)
print(target_node.value)