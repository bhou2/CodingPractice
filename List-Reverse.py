# Iterative method

def reverseList(list):
    
    #Initializing values
    prev = None
    curr = list.head
    nex = curr.getNextNode()
  
    #looping
    while curr:
        #reversing the link
        curr.setNextNode(prev)     

        #moving to next node      
        prev = curr
        curr = nex
        if nex:
            nex = nex.getNextNode()

    #initializing head
    list.head = prev


# Recursive method

def reverse(self,node):

    if node.getNextNode() == None:
         self.head = node
         return
    self.reverse(node.getNextNode())
    temp = node.getNextNode()
    temp.setNextNode(node)
    node.setNextNode(None)
