import csv


class Node:
    _index = 1

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


nodes = []

with open('textbook-grade-chapter-tags/textbook-grade-chapters-full.csv') as file:
    csv_reader = csv.reader(file, delimiter=',')
    next(csv_reader)
    depth = 0
    last_node = None
    for row in csv_reader:
        for index in range(len(row)):
            if row[index]:
                if index == depth:
                    node = Node(row[index], last_node.parent if last_node else None)
                elif index == depth + 1:
                    node = Node(row[index], last_node)
                elif index < depth:
                    for i in range(depth - index):
                        last_node = last_node.parent
                    node = Node(row[index], last_node.parent if last_node else None)
                else:
                    print('缩进异常')
                    break
                depth = index
                nodes.append(node)
                last_node = node

rows = [(node.id, node.get_path(), node.name, node.parent.id if node.parent else None) for node in nodes]
with open('textbook-grade-chapter-tags/textbook-grade-chapters-full-imported.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['ID', 'PATH', 'NAME', 'PARENT_ID'])
    writer.writerows(rows)
