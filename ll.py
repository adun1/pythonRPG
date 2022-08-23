#!/usr/bin/python3
class Node:
	def __init__(self, key=None, value=None):
		self.key = key
		self.value = value
		self.next = None
		
	def getNext():
		return self.next
		
	def setNext(next):
		self.next = next
		return
		
		
class LinkedList:
	def __init__(self):
		self.head = None
		
	def printList():
		return

LENGTH = 3		

LL = LinkedList()

a = []
for i in range(LENGTH):
	a.append(Node(i, i*i))
	
for i in range(LENGTH):
	print("key = " + str(a[i].key) + ", value = " + str(a[i].value))
