#!/usr/bin/python3
import ll
DEFAULTMAX = 100
class Player:
	def __init__(self, name=None, age=None, maxHealth=DEFAULTMAX,startingTokens=0):
		self.name = name
		self.age = age
		self.health = maxHealth
		self.tokens = startingTokens
		self.inventory = ll.LinkedList()
	def getName(self):
		return this.name
	def getAge(self):
		return this.age
	def getHealth(self):
		return self.health
	def setHealth(self, newHealth):
		self.health = newHealth
		return 
	def getTokens(self):
		return this.tokens
	def setTokens(self, newTokens):
		self.tokens = newTokens
		return
	def printInventory(self):
		self.inventory.print()
	
class Room:
	def __init__(self):
		return

user = Player("brian", 1, 90, 1)
