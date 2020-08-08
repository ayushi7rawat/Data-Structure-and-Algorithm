class MaxHeap():

  #we receive a list of items
  def __init__(self,items = []):
    self.heap = [0]
    # we create a heap list and store 0 at first Index
    # we will not use first Index
    for i in items:
      # we will store the items received in items[] in heap
      self.heap.append(i)
      #now we will float them up to thier proper position
      self.float_up(len(self.heap) - 1)

  def push(self,data):
    #append at last location
    self.heap.append(data)
    #heapify
    self.float_up(len(self.heap) - 1)

  def peek(self):
    #check topmost node - stored at index 1
    if self.heap[1]:
      return self.heap[1]
    return False

  def pop(self):
    #case 1: more than 2 Value
    #in that case swap the root to last Value
    if len(self.heap) > 2:
      #swap the max val and last node
      self.swap(1,len(self.heap) - 1)
      #pop the maximum value
      max=self.heap.pop()
      #call the helper fn
      self.bubble_down(1)

    #case 2: when one value, pop it and we have empty heap
    elif len(self.heap) == 2:
      max=self.heap.pop()

    #case 3: no root (pop from empty heap)then return false 
    else:
      max = False
    
    return max

  #helper methods:
  def swap(self,i,j):
    self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

  def float_up(self,index):
    #find parent
    parent = index//2

    if index <= 1:
      return
    
    elif self.heap[index] > self.heap[parent]:
      self.swap(index,parent)
      #recursive call
      self.float_up(parent)

  def bubble_down(self,index): #max heapify
    left = index * 2
    right = index * 2 + 1

    largest = index

    if len(self.heap) > left and self.heap[largest] < self.heap[left]:
      largest = left
    if len(self.heap) > right and self.heap[largest] < self.heap[right]:
      largest = right

    if largest != index:
      self.swap(index,largest)
      #recursive call
      self.bubble_down(largest)
  
  #Warning: this will delete your heap

  def sort_heap(self, order = 0):
    temp = []
    while len(self.heap) > 1:
      temp.append(self.pop())
    if order == 0:
      return temp
    return temp[::-1]


m = MaxHeap([95,3,21])
m.push(10)

print(str(m.heap[1:len(m.heap)]))
print(str(m.pop()))
print(m.sort_heap())
    










  
  


