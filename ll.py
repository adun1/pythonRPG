#!/usr/bin/python3
class Node:
	def __init__(self, key=None, value=None):
		self.key = key
		self.value = value
		self.next = None		
	def getNext(self):
		return self.next
	def getKey(self):
		return self.key
	def getValue(self):
		return self.value
	def setNext(self,next):
		self.next = next
		return
		
		
class LinkedList:
	def __init__(self):
		self.head = None
	def append(self, item):
		if self.head is None:
			self.head = item
			return
		current = self.head
		while current.getNext() is not None:
			current = current.getNext()
		current.setNext(item)
	def print(self):
		print("Printing List")
		current = self.head
		while current is not None:
			print("key = " + str(current.getKey()) + ", value = " + str(current.getValue()))
			current = current.getNext()
		return

LENGTH = 3		

LL = LinkedList()

a = []
for i in range(LENGTH):
	#a.append(Node(i, i*i))
	LL.append(Node(i, i*i))
LL.print()
	

	
#for i in range(LENGTH):
	#print("key = " + str(a[i].key) + ", value = " + str(a[i].value))
