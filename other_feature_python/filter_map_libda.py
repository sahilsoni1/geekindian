#use lambda with filter
numbers=[1,2,3,4,5,6,7,8,9,10]
# This will only return true for even numbers (because x%2 is 0, or False, 
# for odd numbers) 
even_number = filter(lambda x: x%2 == 0, numbers) 
print(*even_number)

even_number = map(lambda x: x%2 == 0, numbers) 
print(*even_number)
print(type(even_number))
print([ x for x in numbers if x%2 == 0]) 

f=range(10,20)
print(*f)
print(f[0])