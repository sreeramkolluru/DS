class Node():

    def __init__(self,data=None,previous=None,next=None):
        self.previous=previous
        self.data=data
        self.next=next

    def get_next(self):
        return self.next

    def  set_next(self,next):
        self.next=next

    def get_previous(self):
        return self.previous

    def set_previous(self,previous):
        self.previous=previous

    def get_data(self):
        return self.data

    def set_data(self,data):
        self.data=data

    def has_next(self):
        if self.next!=None:
            return True
        else:
            return False

    def has_previous(self):
        if self.previous!=None:
            return True
        else:
            return False

class dllist():

    def __init__(self):
        self.head=None
        self.tail=None


    def insert_at_beginning(self,data):
        n = Node(data)
        if self.head==None:
            self.head=self.tail=n
        else:
            n.set_data(data)
            n.set_next(self.head)
            self.head.set_previous(n)
            n.set_previous(None)
            self.head=n


    def insert_at_ending(self,data):
        n=Node(data)
        temp=self.head
        if self.head==None:
            self.head=self.tail=n
        else:
            self.tail.set_next(n)
            n.set_previous(self.tail)
            n.set_data(data)
            n.set_next(None)
            self.tail=n


    def insert_in_middle(self,data,position):
        n=Node(data)
        pos=1
        n1=self.head
        n2=None
        if self.head==None:
            self.head=self.tail=n
        else:
            while n1.get_next()!=None:
                pos=pos+1
                n1=n1.get_next()
                n2=n1.get_next()
                if pos==position:
                    break
            n.set_previous(n1)
            n1.set_next(n)
            n.set_next(n2)
            if n2!=None:
                n2.set_previous(n)

    def traverse_dl(self):
        n=self.head
        print "This is the data in head position node: "+str(n.get_data())
        print "This is the next of head data: "+str(n.get_next())
        print "This is the head: " + str(n)
        print "\n"

        i=0
        while n.get_next()!=None:
            i=i+1
            n=n.get_next()
            print "The node is of position: "+str(i)
            print "The previous of Node is: "+str(n.get_previous())
            print "The data of Node is: "+str(n.get_data())
            print "The next of Node is: "+str(n.get_next())
            print "\n"


dl=dllist()
dl.insert_at_beginning(1)
dl.insert_in_middle(2,2)
dl.insert_in_middle(3,3)
dl.insert_in_middle(4,4)
dl.insert_in_middle(5,5)
# dl.insert_at_ending(6)
dl.traverse_dl()