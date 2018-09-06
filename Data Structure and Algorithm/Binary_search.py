class Node(object):
    def __init__(self,data):
        self.data = data
        self.leftChild=None
        self.rightChild=None


class BinarySearchTree(object):

    def __init__(self):
        self.root=None

    def insert(self,data):
        if not self.root:
            self.root=Node(data)
        else:
            self.insertNode(data,self.root)
    # O (log N)--> If the tree is balanced otherwise it can reduced to O(N)  --> AVL Tress are needed
    def insertNode(self,data,node):
        if data < node.data:
            if node.leftChild:
                self.insertNode(data,node.leftChild)
            else:
                node.leftChild=Node(data)
        else:
            if node.rightChild:
                self.insertNode(data,node.rightChild)
            else:
                node.rightChild=Node(data)

    def removeNode(self,data,node):
        if not node:
            return node
        
        if data < node.data:
            node.leftChild = self.removeNode(data,node.leftChild)

        elif data > node.data:
            node.rightChild = self.removeNode(data,node.rightChild)
        else:
            if not node.leftChild and node.rightChild:
                print("Removing a Leaf Node....")
                del node
                return None
            if not node.leftChild:
                print("Removing a node with Right Child ...")
                tempNode=node.rightChild
                del node
                return tempNode
            elif not node.rightChild:
                print("Removing a node with Left Child ...")
                tempNode=node.leftChild
                del node
                return tempNode

            print("Removing a node with two children")
            tempNode=self.getPredeccor(node.leftChild)
            node.data=tempNode.data
            node.leftChild=self.removeNode(tempNode.data, node.leftChild)
        return node
    
    def getPredeccor(self,node):
        if node.rightChild:
            return self.getPredeccor(node.rightChild)
        return node

    def remove(self,data):
        if self.root:
            self.root = self.removeNode(data,self.root)

    def getMinvalue(self):
        if self.root:
            return self.getMin(self.root)

    def getMin(self,node):
        if node.leftChild:
            return self.getMin(node.leftChild)
        return node.data

    def getMaxvalue(self):
        if self.root:
            return self.getMax(self.root)

    def getMax(self,node):
        if node.rightChild:
            return self.getMax(node.rightChild)
        return node.data

    def traversing(self):
        if self.root:
            return self.tranverInOrder(self.root)

    def tranverInOrder(self, node):
        if node.leftChild:
            self.tranverInOrder(node.leftChild)

        print("%s" % node.data)

        if node.rightChild:
            self.tranverInOrder(node.rightChild)

bst = BinarySearchTree()
bst.insert(10)
bst.insert(13)
bst.insert(5)
bst.insert(14)
bst.traversing()
print("The maximum value is ",bst.getMaxvalue())
print("The minimum value is ",bst.getMinvalue())

bst.remove(10)
bst.traversing()
