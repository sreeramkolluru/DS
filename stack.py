class Stack:
    def __init__(self,limit):
        self.listitems=[]
        self.max_limit=limit

    def is_empty(self):
        return len(self.listitems)==0

    def push(self,data):
        if len(self.listitems)==self.max_limit:
            print 'Stack is full. Sorry! Cant insert anymore. Overflow alert'
        else:
            self.listitems.append(data)

    def pop(self):
        if len(self.listitems) == 0:
            print 'Stack is empty. Sorry! Underflow alert'
        else:
            size=self.stack_size()
            # self.listitems=self.listitems[0:size-2]
            return self.listitems.pop()

    def peek(self):
        if len(self.listitems) == 0:
            print 'Stack is empty. Sorry! Underflow alert'
        else:
            size=self.stack_size()
            # self.listitems=self.listitems[0:size-2]
            return self.listitems[-1]


    def stack_size(self):
        return len(self.listitems)

class stack_rdoubling():
    # global counter = 0
    def init(self,limit=10):
        self.stacklist=limit*[None]
        self.limit=limit


    def is_empty(self):
        return len(self.stacklist)

    def push(self,data):
        if counter!=len(self.stacklist):
            self.stacklist[counter]=data
        counter=counter+1
        else:
            resize(2*counter)
            self.stacklist[counter] = data

    def pop(self):

    def size(self):

    def resize(self,new_length):
        new_stack=self.stacklist
        self.


