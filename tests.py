#!/usr/bin/python3
import ll

LENGTH = 3		
LL = ll.LinkedList()
for i in range(LENGTH):
	LL.append(ll.Node(i, i*i))

#debugging
LL.print()
LL.remove(LL.findNode(0))
LL.append(ll.Node(3, 9))
LL.remove(LL.findNode(2))
LL.append(ll.Node(-1, 1))
LL.remove(LL.findNode(-1))
LL.print()
