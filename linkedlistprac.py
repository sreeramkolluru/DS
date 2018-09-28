#Find nth node from the end of a linked list

from wxPython._wx import true, false


class Node:
    def __init__(self):
        self.data=None
        self.next=None

    def set_data(self,data):
        self.data=data

    def set_next(self,next):
        self.next=next

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

# temp = Node()
# temp.set_data(100)
# temp.set_next(101)
# print temp.get_data()
# print temp.get_next()

class linkedList:

    counter=0
    singleNode1=None
    count = 1
    def __init__(self):
        self.head=None

    def isEmpty(self):
        return self.head==None

    # def addItem(self,data):
    #     singleNode = Node()
    #     previousNode = linkedList.singleNode1
    #     if linkedList.counter==0:
    #         singleNode.set_data(data)
    #         singleNode.set_next(None)
    #
    #     else:
    #         singleNode.set_data(data)
    #         singleNode.set_next(previousNode)
    #     self.head=singleNode
    #     singleNode1=singleNode
    #     print self.head
    #     print "The node data is: "+str(singleNode.get_data())
    #     print "The node next pointer is: "+str(singleNode.get_next())
    #     linkedList.counter = linkedList.counter + 1

    def addItem2(self,data):
        singleNode = Node()
        singleNode.set_data(data)
        singleNode.set_next(self.head)
        self.head=singleNode

    def sizeOfList(self):
        firstNode=self.head
        while firstNode.get_next()!=None:
            linkedList.count = linkedList.count + 1
            firstNode=firstNode.get_next()
        return linkedList.count

    def searchNode(self,data):
        found=false
        firstNode=self.head
        size1=self.sizeOfList()
        while size1 !=0 and not found:
            if firstNode.get_data()!=data:
                print "the data is not found: "+ str(firstNode.get_data())
                firstNode=firstNode.get_next()

            else:
                print  "the data matches: "+str(firstNode.get_data())
                found = true

            size1=size1-1

    def removeNode(self,data):
        found = false
        firstNode = self.head
        size1 = self.sizeOfList()
        previousNode=None
        while size1 != 0 and not found:
            if firstNode.get_data() != data:
                print "the data is not found: " + str(firstNode.get_data())
                previousNode=firstNode
                firstNode = firstNode.get_next()

            else:
                print  "the data matches: " + str(firstNode.get_data())
                previousNode.set_next(firstNode.get_next())
                found = true

            size1 = size1 - 1

    def nthlast(self):
        hashdict={}
        firstNode=self.head


llist=linkedList()
# llist.addItem2(1)
# llist.addItem2(2)
# llist.addItem2(3)
# llist.addItem2(4)
llist.addItem2(1)
llist.addItem2(2)
llist.addItem2(3)
llist.addItem2(4)
# size=llist.sizeOfList()
# llist.removeNode(3)
# llist.searchNode(1)
# print size

