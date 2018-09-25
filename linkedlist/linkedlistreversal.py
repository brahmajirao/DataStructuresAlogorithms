class Node(object):
    def __init__(self, value):
        self.value = value
        self.next_node = None

def reversal(node):
    current_node = node
    previous_node = None
    next_node = None
    while current_node:
        next_node = current_node.next_node
        current_node.next_node = previous_node
        previous_node = current_node
        current_node = next_node

    return previous_node

# Create a list of 4 nodes
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

# Set up order a,b,c,d with values 1,2,3,4
a.next_node = b
b.next_node = c
c.next_node = d

print (a.next_node.value)
print (b.next_node.value)
print (c.next_node.value)

reversal(a)

print (d.next_node.value)
print (c.next_node.value)
print (b.next_node.value)