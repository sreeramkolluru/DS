
class Node():
    def __init__(self):
        self.data=None
        self.next=None

    def setData(self,data):
        self.data=data

    def setNext(self,next):
        self.next=next

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

class circularlinkedlist():

    def __init__(self):
        self.head=None

    def appendNode(self,data):
        newNode = Node()
        newNode.setData(data)
        newNode.setNext(newNode)
        currentNode = self.head
        if self.head==None:
            # newNode.setNext(self.head)
            self.head=newNode

        # elif self.head.getNext()==self.head:
        #     newNode.setNext(self.head)
        #     self.head.setNext(newNode)

        else:
            while currentNode.getNext()!=self.head:
                currentNode=currentNode.getNext()
            newNode.setNext(self.head)
            currentNode.setNext(newNode)

    def insertBegin(self,data):#this works only if the cll already has some attributes
        newNode = Node()
        newNode.setData(data)
        newNode.setNext(self.head)
        currentNode=self.head
        while currentNode.getNext()!=self.head:
            currentNode=currentNode.getNext()
        currentNode.setNext(newNode)
        self.head=newNode







    def printCLL(self):
        currentNode=self.head
        # currentNode.getNext() != self.head
        print currentNode.getData()
        while currentNode.getNext() != self.head:
            currentNode = currentNode.getNext()
            print currentNode.getData()



c1=circularlinkedlist()
c1.appendNode(12)
c1.appendNode(13)
c1.appendNode(14)
c1.appendNode(15)
c1.insertBegin(11)
c1.printCLL()




