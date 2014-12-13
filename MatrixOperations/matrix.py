# matrix rotation


def print_matrix(m):
	for row in matrix:
		print row
	print '\n'

def rotate(m):
	for row in range(len(m)/2):
		for col in range(row, len(m)-row-1):
			temp = m[row][col]
			m[row][col] = m[col][len(m)-1-row]
			m[col][len(m)-1-row] = m[len(m)-1-row][len(m)-1-col]
			m[len(m)-1-row][len(m)-1-col] = m[len(m)-1-col][row]
			m[len(m)-1-col][row] = temp

# rotate(matrix)
# print matrix


def rotatecw(m):
	w = len(m) - 1
	i = 0
	while i < w - 1:
		j = i
		while j < w - i:
			temp = m[j][i]
			m[j][i] = m[w-i][j]
			m[w-i][j] = m[w-j][w-i]
			m[w-j][w-i] = m[i][w-j]
			m[i][w-j] = temp
			j += 1
		i += 1
	return m


def rotateccw(m):
	w = len(m) - 1
	i = 0
	while i < w - 1:
		j = i
		while j < w - i:
			temp = m[j][i]
			m[j][i] = m[i][w-j]
			m[i][w-j] = m[w-j][w-i]
			m[w-j][w-i] = m[w-i][j]
			m[w-i][j] = temp
			j += 1
		i += 1
	return m


matrix4 = [
['A', 'B', 'C', 'D'], 
['L', 'M', 'N', 'E'], 
['K', 'P', 'O', 'F'],
['J', 'I', 'H', 'G'] ]

matrix5 = [
['A', 'B', 'C', 'D', 'E'], 
['P', 'Q', 'R', 'S', 'F'], 
['O', 'X', 'Y', 'T', 'G'],
['N', 'W', 'V', 'U', 'H'],
['M', 'L', 'K', 'J', 'I' ]]


print_matrix(matrix)
rotateccw(matrix)
print_matrix(matrix)
rotatecw(matrix)
print_matrix(matrix)
rotatecw(matrix)
print_matrix(matrix)