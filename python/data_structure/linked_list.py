class Node:
    def __init__(self, val = None):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        printval = self.head
        while printval is not None:
            print(printval.val)
            printval = printval.next

    def atBeginning(self, newData):
        NewNode = Node(newData)
        NewNode.next = self.head
        self.head = NewNode

    def atEnd(self, newData):
        if self.head is None:
            newNode = Node(newData)
            self.head = newNode
        else:
            node = self.head
            while(node.next):
                node = self.head.next
            newNode = Node(newdata)
            node.next = newNode

    def inBetween(self, newData, middleNode):
        if middleNode is None:
            pass
        else:
            newNode = Node(newData)
            newNode.next = middleNode.next
            middleNode.next = newNode

    def removeNode(self, removeKey):
        head = self.head
        if head is not None:
            if head.val == removeKey:
                self.head = head.next
                head = None
            else:
                pass
        else:
            pass



linkedlist = LinkedList()
node1 = Node("elsdo")
node2 = Node("masodik")
node3 = Node("harmadik")

linkedlist.head = node1
node1.next = node2
node2.next = node3

linkedlist.print()