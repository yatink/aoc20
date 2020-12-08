
input = """<paste problem input here>"""

input = input.split("\n")

height = len(input)
width = len(input[0])

x_coords = xrange(0,10000, 2)
y_coords = (i % width for i in range(0, 10000))
#coords = enumerate(i % width for i in range(0,100000,1))

count = 0
for i,j in zip(x_coords, y_coords):
    if i >= height:
        break
    try:
        if input[i][j] == '#':
            count += 1
    except IndexError:
        import pdb; pdb.set_trace()

print count
