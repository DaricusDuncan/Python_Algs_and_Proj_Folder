class Node(object):
    def __init__(self, data = None, next = None):
        self.data = data;
        self.next = next;

    def __str__(self):
        return str(self.data)


class LinkedList(object):
    def __init__(self,head = None):
        self.head = head
        self.size = 0

    def prepend(self,data):
        newNode = Node(data);
        newNode.next = self.head
        self.head = newNode
        self.size += 1

    def append(self,data):
        self.size += 1

        if not (self.head):
            newNode = Node(data)
            self.head = newNode
        else:
            current = self.head
            while(current.next != None):
                current = current.next
            current.next = Node(data)

    def getSize(self):

        return (self.size)
            

    
        
