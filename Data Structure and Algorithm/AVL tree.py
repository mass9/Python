class Node(object):
    def __init__(self, data):
        self.data = data
        self.height = 0
        self.leftChild = None
        self.rightChild = None


class AVLTrees(object):
    def __init__(self):
        self.root = None

    def remove(self, data):
        if self.root:
            self.root = self.removeNode(data, self.root)



    def insert(self, data):
        self.root = self.insertNode(data, self.root)

    def insertNode(self, data, node):

        if not node:
            return Node(data)

        if data < node.data:
            node.leftChild = self.insertNode(data, node.leftChild)
        else:
            node.rightChild = self.insertNode(data, node.rightChild)

        node.height = max(self.calcHeight(node.leftChild), self.calcHeight(node.rightChild)) + 1

        return self.settleViolation(data, node)

    def removeNode(self, data, node):
        if not node:
            return node

        if data < node.data:
            node.leftChild = self.removeNode(data, node.leftChild)

        elif data > node.data:
            node.rightChild = self.removeNode(data, node.rightChild)
        else:
            if not node.leftChild and not node.rightChild:
                print("Removing a Leaf Node....")
                del node
                return None

            if not node.leftChild:
                print("Removing a node with a Right Child ...")
                tempNode = node.rightChild
                del node
                return tempNode

            elif not node.rightChild:
                print("Removing a node with a Left Child ...")
                tempNode = node.leftChild
                del node
                return tempNode

            print("Removing a node with two children")
            tempNode = self.getPredeccor(node.leftChild)
            node.data = tempNode.data
            node.leftChild = self.removeNode(tempNode.data, node.leftChild)

        if not node:
            return node
        node.height = max(self.calcHeight(node.leftChild), self.calcHeight(node.rightChild)) + 1

        balance = self.calcBalance(node)

        if balance > 1 and self.calcBalance(node.leftChild) >= 0:
            return self.rotateRight(node)

        if balance < -1 and self.calcBalance(node.leftChild) <= 0:
            return self.rotateLeft(node)

        if balance > 1 and self.calcBalance(node.rightChild) < 0:
            node.leftChild = self.rotateLeft(node.leftChild)
            return self.rotateRight(node)

        if balance < -1 and self.calcBalance(node.rightChild) > 0:
            node.rightChild = self.rotateRight(node.rightChild)
            return self.rotateLeft(node)

        return node

    def getPredeccor(self, node):
        if node.rightChild:
            return self.getPredeccor(node.rightChild)
        return node

    def settleViolation(self, data, node):

        balance = self.calcBalance(node)

        if balance > 1 and data < node.leftChild.data:
            print("The Left Left heavy situation...")
            return self.rotateRight(node)

        if balance < -1 and data > node.rightChild.data:
            print("The Right right heavy situation...")
            return self.rotateLeft(node)

        if balance > 1 and data > node.leftChild.data:
            print("The Left right heavy situation...")
            node.leftChild = self.rotateLeft(node.leftChild)
            return self.rotateRight(node)

        if balance < -1 and data < node.rightChild.data:
            print("The right Left heavy situation...")
            node.rightChild = self.rotateRight(node.rightChild)
            return self.rotateLeft(node)
        return node

    def calcHeight(self, node):
        if not node:
            return -1
        return node.height

    def calcBalance(self, node):
        if not node:
            return 0
        return self.calcHeight(node.leftChild) - self.calcHeight(node.rightChild)

    def tranverse(self):
        if self.root:
            self.tranverseInroder(self.root)

    def tranverseInroder(self, node):
        if node.leftChild:
            self.tranverseInroder(node.leftChild)

        print("%s" % node.data)

        if node.rightChild:
            self.tranverseInroder(node.rightChild)

    def rotateRight(self, node):
        print("Rotating to the right on node", node.data)
        tempLeftChild = node.leftChild
        t = tempLeftChild.rightChild

        tempLeftChild.rightChild = node

        node.leftChild = t

        node.height = max(self.calcHeight(node.leftChild), self.calcHeight(node.rightChild)) + 1

        tempLeftChild.height = max(self.calcHeight(tempLeftChild.leftChild),
                                   self.calcHeight(tempLeftChild.rightChild)) + 1

        return tempLeftChild

    def rotateLeft(self, node):
        print("Rotating to the Left on node", node.data)

        tempRightChild = node.rightChild
        t = tempRightChild.leftChild

        tempRightChild.leftChild = node

        node.rightChild = t

        node.height = max(self.calcHeight(node.leftChild), self.calcHeight(node.rightChild)) + 1

        tempRightChild.height = max(self.calcHeight(tempRightChild.leftChild),
                                    self.calcHeight(tempRightChild.rightChild)) + 1

        return tempRightChild


avl = AVLTrees()

avl.insert(10)
avl.insert(20)
avl.insert(15)
avl.insert(6)
avl.insert(99)
avl.tranverse()
avl.remove(99)
avl.insert(120)
avl.insert(85)
avl.insert(11)
avl.insert(79)
avl.remove(11)
avl.insert(60)
avl.insert(305)
avl.insert(61)

avl.remove(60)
avl.remove(79)
avl.tranverse()
