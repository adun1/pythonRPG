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
	def remove(self, item):
		#case front item (covers only item and head)
		if item == self.head:
			self.head = self.head.getNext()
			return	
		current = self.head
		#prev
		#after
		#delNode
		while current.getNext() is not None:
			prev = current
			delNode = current.getNext()
			after = current.getNext().getNext()
			if delNode == item:
				break;
			current = current.getNext()
		#case not found
		if delNode is None:
			return
		#found
		prev.setNext(after)
		delNode = None
		
	def findNode(self, key):
		current = self.head
		while current is not None:
			if current.key == key:
				return current
			current = current.getNext()
		return None
	
			

LENGTH = 3		

LL = LinkedList()

a = []
for i in range(LENGTH):
	#a.append(Node(i, i*i))
	LL.append(Node(i, i*i))

#debugging
LL.print()
LL.remove(LL.findNode(0))
LL.append(Node(3, 9))
LL.remove(LL.findNode(2))
LL.append(Node(-1, 1))
LL.remove(LL.findNode(-1))
LL.print()

	

	
#for i in range(LENGTH):
	#print("key = " + str(a[i].key) + ", value = " + str(a[i].value))
