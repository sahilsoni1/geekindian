#Normal_code
cube = []
for x in range(10):
    cube.append(x**3)

print(cube)
#Comprehension_code
cubes=[x**3 for x in range(10)]
print(cubes)

combs=[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(combs)
print(type(combs))

combs1 = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs1.append((x, y))
print(combs1)

combs=list(zip(*combs))
print(combs)
combs2=combs
combs2=list(zip(*combs2))
print(combs2)



everything = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 ] 
print([ x for x in everything if x%2 == 0])  



person = {"name": "James", "camera": "nikon", "handedness": "lefty", "baseball_team": "angels", "instrument": "guitar"}

print("%(name)s, %(camera)s, %(baseball_team)s" % person)  
 

person["height"] = 1.6 
person["weight"] = 80 

print("%(name)s, %(camera)s, %(baseball_team)s, %(height).2f, %(weight).1f" % person)  