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
