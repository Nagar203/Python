s1 = "Addition: {x} + {y} = {z}".format(x=10,y=20,z=30)


x, y, z = 1, 2, 3
s2 = "Addition: {} + {} = {}".format(x,y,z)

x, y, z = 100, 200, 300
s3 = f'Addition: {x} + {y} = {z}'

data = {'x': 'this is x', 'y': 'this is y'}
s4 = 'Information: {x}, {y}'.format(**data)

print(s1)
print(s2)
print(s3)
print(s4)