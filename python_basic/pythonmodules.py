import Fridge
if __name__ == '__main__':
	pass
#	print(dir(Fridge))# shows all of the properties of the  Fridge object
#	print(dir(Fridge.Fridge()))# shows all of the properties of the  Fridge.Fridge() object
	f =Fridge.Fridge({"eggs":6, "milk":4, "cheese":3}) # from Fridge.py file call Fridge class
	print("items before updation:%s"%str(f.items))  #print items object of class
	print("grape has added ? %s"%f.add_one("grape")) # add item in items object
	f.add_many({"mushroom":5, "tomato":3})#add multiple items in items object
	print("cheese quanity is five ? %s"%f.has("cheese", 5))# check cheese quantity is 5

