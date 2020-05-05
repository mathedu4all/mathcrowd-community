import re
import csv


class Node:
    _index = 10000

    def __init__(self, name, parent):
        self.id = Node._index
        Node._index += 1
        self.name = name
        self.parent = parent

    def get_path(self):
        parent = self.parent
        if parent is not None:
            return self.parent.get_path() + '->' + self.name
        else:
            return self.name


with open('knowledge-tags/knowledge-nodes-full.md', 'r') as file:
    input_text = file.read()
    line = re.compile(r'( *)\* (.*)\n?')
    depth = 0
    nodes = []
    last_node = None
    for indent, name in line.findall(input_text):

        indent = int(len(indent) / 2)
        if indent == depth:
            node = Node(name, last_node.parent if last_node else None)
        elif indent == depth + 1:
            node = Node(name, last_node)
        elif indent < depth:
            for i in range(depth - indent):
                last_node = last_node.parent
            node = Node(name, last_node.parent if last_node else None)
        else:
            print('缩进异常')
            break
        depth = indent
        nodes.append(node)
        last_node = node

rows = [(node.id, node.get_path(), node.name, node.parent.id if node.parent else None) for node in nodes]
with open('knowledge-tags/knowledge-nodes-full.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['ID', 'PATH', 'NAME', 'PARENT_ID'])
    writer.writerows(rows)
