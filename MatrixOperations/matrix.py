# matrix rotation

# row0 = ['a', 'b', 'c', 'd', 'e']
# row1 = ['f', 'g', 'h', 'i', 'j']
# row2 = ['k', 'l', 'm','n', 'o']
# row3 = ['p', 'q', 'r', 's', 't']
# row4 = ['u', 'v', 'w', 'x', 'y']

# matrix = [row0, row1, row2, row3, row4]

matrix = [ ['A', 'B'], ['D', 'C'] ]

print matrix

def rotate(m):
	for row in range(len(m)/2):
		for col in range(row, len(m)-row-1):
			temp = m[row][col]
			m[row][col] = m[col][len(m)-1-row]
			m[col][len(m)-1-row] = m[len(m)-1-row][len(m)-1-col]
			m[len(m)-1-row][len(m)-1-col] = m[len(m)-1-col][row]
			m[len(m)-1-col][row] = temp

rotate(matrix)
print matrix
