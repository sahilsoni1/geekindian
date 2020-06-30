#!/usr/bin/env python3.7.0
class Fridge:
	"""
	This class implements a fridge where ingredients can be
 	added and removed individually, or in groups.
	"""

	def __init__(self, items={}):
		if type(items) != type({}):
			raise TypeError("Fridge requires a dictionary but was given %s" %type(items))
		self.items = items
		return

	def __add_multi(self,food_name,quantity):
		if(not food_name in self.items):
			self.items[food_name]=0
		self.items[food_name] = self.items[food_name] + quantity

	def add_one(self, food_name):
		if type(food_name) != type(""):
			raise TypeError("add_one requires a String, given a %s"%type(food_name))
		else:
			self.__add_multi(food_name,1)
		return True


	def add_many(self,food_dict):
		if type(food_dict)!=type({}):
			raise TypeError("add_many requires a diretonary,got a %s"%type(food_name))
		for item in food_dict.keys():
			self.__add_multi(item,food_dict[item])
			return

	def has(self,food_name,quantity=1):
		return self.has_various({food_name:quantity})


	def has_various(self,foods):
		try:
			for food in foods.keys():
				if self.items[food] <foods[food]:
					return False
				return True
		except KeyError:
			return False


	def __get_multi(self,food_name,quantity):
		try:
			if(self.items[food_name] is None):
				return False
			return True	
		except KeyError:
			return False
	def get_one(self,food_name):
		if type(food_name) != type(""):
			raise Typeerror("get_one requires a String< given a %s" %type(food_name))
		else:
			result=self.__get_multi(food_name, 1)
		return result

	def get_many(self, food_dict):
		if self.has_various(food_dict):
			foods_removed ={}
			for item in food_dict.keys():
				foods_removed[item]=self.__get_multi(item,food_dict[item])
			return foods_removed



	def	get_ingredients(self,food):
		try:
				ingredients=self.get_many(food.__ingredients__())
		except AttributeError:
			return False
		if ingredients !=False:
			return ingredients
