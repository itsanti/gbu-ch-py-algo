"""HW9 - Task 2

Закодируйте любую строку по алгоритму Хаффмана.
"""

from collections import Counter, deque
from hw9.Node import Node

msg = 'beep boop beer!'

friq = Counter(msg)
friq = friq.most_common()
friq.reverse()

deq = deque(friq)

nodes = deque()
for node in deq:
    nodes.append(Node(node[0], node[1]))

print(deq)


def gen_tree(nodes):
    if len(nodes) < 2:
        return nodes

    first = nodes.popleft()
    second = nodes.popleft()

    new_node = Node(None, first.weight + second.weight, first, second)

    if len(nodes) > 0:
        ix = 0
        for i, node in enumerate(nodes):
            if new_node.weight == node.weight:
                nodes.insert(i, new_node)
                break
            elif new_node.weight > node.weight:
                ix = i + 1
        else:
            if ix > 0:
                nodes.append(new_node)
            else:
                nodes.appendleft(new_node)
    else:
        nodes.append(new_node)

    gen_tree(nodes)


gen_tree(nodes)

table = {}


def get_table(node, p=''):
    if node.data is not None:
        table[node.data] = p
    if node.left is not None:
        get_table(node.left, p=(p + '0'))
    if node.right is not None:
        get_table(node.right, p=(p + '1'))


get_table(nodes[0])
print(table)

code = ''
code_sep = []
for char in msg:
    code += table[char]
    code_sep.append(table[char])

print(code)
print('|'.join(code_sep))

'''
deque([('!', 1), ('r', 1), ('o', 2), (' ', 2), ('p', 2), ('b', 3), ('e', 4)])
{'b': '00', ' ': '010', 'p': '011', '!': '1000', 'r': '1001', 'o': '101', 'e': '11'}
0011110110100010110101101000111110011000
00|11|11|011|010|00|101|101|011|010|00|11|11|1001|1000
'''
