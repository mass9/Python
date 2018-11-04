from pprint import pprint

class node:

    def __init__(self, name, contents = []):
        self.name = name
        self.contents = contents[:]

    def __repr__(self):
        return (
                'node(' + repr(self.name) + ',' + repr(self.contents) + ')')

trees = [
        node('node1'),
        node('node2',[node('node2-1')]),
        node('node3',[node('node3-1')]),
        ]
pprint(trees)
