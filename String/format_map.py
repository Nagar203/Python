data = {'x': 'this is x', 'y': 'this is y'}
s1 = 'Information: {x}, {y}'.format(**data) # format.map(data)
s2 = 'Information: {x}, {y}'.format_map(data) # format_map(data)

data = {'x':10, 'y':20}
s3 = 'Information: {x}, {y}'.format(**data)
s4 = 'Information: {x}, {y}'.format_map(data)

print(s1)
print(s2)
print(s3)
print(s4)