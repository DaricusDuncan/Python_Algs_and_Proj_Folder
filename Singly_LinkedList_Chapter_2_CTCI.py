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

    def removeByPosition(self,position):
        current = self.head
        count = 1

        if not (self.head):
            return("Add elements to the LinkedList first")
        elif(position == 1):
            origHead = self.head
            newHead = self.head
            self.head = newHead.next
        elif(position >= 1):
            while(count != (position-1)):
                current = current.next
                count+=1
        current.next = current.next.next
        self.size -= 1


    def removeDuplicates(self):
        temp = self.head
        temp2 = self.head.next
        count = 0

        if(self.size == 0):
            return("Add elements to LinkedList")
        elif(self.size == 1):
            return("No duplicates")
        elif(self.size == 2):
            if(temp.data == temp2.data):
                temp.next = temp.next.next
                self.size -= 1
        else:
 #           temp = self.head
 #           temp2 = self.head.next
            
            while (temp):
                #print("Temp1: " + str(temp.data))
                temp2 = temp
                while (temp2.next):
                    #print("Temp2: " + str(temp2.data))
                    if (temp.data == temp2.next.data):
                        temp2.next = temp2.next.next
                        self.size -= 1
                    else:
                       temp2 = temp2.next
                temp = temp.next
            
            
        
            
        
                
                
                
                
             
             
        



linked = LinkedList()
linked.append(1)
linked.append(2)
linked.append(3)
linked.append(4)
linked.append(2)
linked.append(3)
linked.append(4)


# 1 2 3 4
# 0 1 2 3

    
        
