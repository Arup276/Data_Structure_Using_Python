
# coding: utf-8

# ## Creating Node
# 

# In[1]:


class Node(object):
    def __init__(self,value):
        self.value = value # set the value in value field and next to null
        self.next = None
    


# ## Creating Linked List 

# In[36]:


class LinkedList(object):
    """Single Linked List"""
    def __init__(self,head = None):
        self.head = head # creating head ,if it's not passed then set it to null
        
    # append last
    def append(self,data):
        new_ele = Node(data)
        if self.head is None: # If we don't have head then set the new element as head 
            self.head = new_ele
            return
        current = self.head # else go the last of linked list and add the new element
        while current.next: 
            current = current.next
        current.next = new_ele 
    
    
    # Append in given index
    def pappend(self,index,data):
        new_node = Node(data)
        current = self.head
        if index > self.lenght() or index == 0:
            return "out of range"
        i = 0
        if self.head is None:
            self.head = new_node
            return
        
        while True:
            if index == i+1:
                print(i)
                new_node.next = current.next # first assign the next noxt add in new node then address of new node in previous node
                current.next = new_node
                break
            i = i+1
            current = current.next
                    
    # Display the linked list
    def show(self):
        pointer = self.head
        while pointer:
            print(pointer.value)
            pointer = pointer.next
             
    # remove 
    def remove(self,data):
        current = self.head
        
        if current and current.value == data:
            self.head=current.next
            current.value = None
        else:
            while current.next:
                #print(current.next.value)
                if current.next.value == data:
                    current.next = current.next.next
                else:
                    current = current.next
        return self.show()
    
    # calculating lenght
    def lenght(self):
        i = 0
        cur = self.head
        while cur:
            i+=1
            cur = cur.next
        return i
    
    
    # remove element from given index
    def dposition(self,index):
        cur = self.head
        if index >= self.lenght():
            return "index out of range"
        if index == 0:
            self.head = cur.next
            print(cur.value)
            cur.value = None
            
        else:
            i = 0
            while i < self.lenght():
                if i+1 == index:
                    print(cur.next.value)
                    cur.next.value = None
                    cur.next = cur.next.next
                    
                    return 
                else:
                    i+=1
                    cur = cur.next
            return cur.value
        

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)

