#http://www.geeksforgeeks.org/write-a-c-function-to-detect-loop-in-a-linked-list/

class Node:
  #constructor to initialize the node object
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  #function to nitialize head
  def __init__(self):
    self.head = None

  #function to insert a new node at the beginning
  def push(self, new_data):
    new_node = Node(new_data)
    new_node.next = self.head
    self.head = new_node

  #utility function to print the linkd list
  def printList(self):
    temp =self.head
    while temp:
      print temp.data,
      temp = temp.next

  def detectLoop(self):
    slow_p = self.head
    fast_p = self.head
    while (slow_p and fast_p and fast_p.next):
      slow_p = slow_p.next
      fast_p = fast_p.next.next
      if slow_p == fast_p:
        print "Found Loop"
        return

#driver program for testing
llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(10)
llist.printList()

# Create a loop for testing
llist.head.next.next.next.next = llist.head
#llist.printList()
llist.detectLoop()
      
