
"""
Find a path from S to E!
S = start
E = end
# = wall
* = path
"""
 
maze = ["########",
        "#      E",
        "# # ####",
        "# #   ##",
        "# # ####",
        "#      S",
        "########"]
 
# example solution
solution = ["########",
            "#  ****E",
            "# #*####",
            "# #*  ##",
            "# #*####",
            "#  ****S",
            "########"]

class Node:
	def __init__(self, pos=None, parent=None, F = None):
		self.pos = pos
		self.parent = parent
		self.G = None


class Maze:

	def __init__(self, maze=maze):
		self.maze = maze
		self.width = len(maze[0])  
		self.height = len(maze)
		self.start = Node(self.find_start())
		self.end = Node(self.find_end())
		self.md = self.manhattan_distance(self.start, self.end)
		self.start.G = 0
		self.end.G = self.md

	def find_start(self):
		for y in range(len(self.maze)):
			for x in range(len(self.maze[y])):
				if self.maze[y][x] == "S":
					return (x, y)
		return None

	def find_end(self):
		for y in range(len(self.maze)):
			for x in range(len(self.maze[y])):
				if self.maze[y][x] == "E":
					return (x, y)
		return None

	def manhattan_distance(self, start, end):
		horiz_dist = abs(start.pos[0] - end.pos[0])
		vert_dist = abs(start.pos[1] - end.pos[1])
		return horiz_dist + vert_dist

	def get_adjacent(self, current):
		adj = []
		moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

		for move in moves:
			new_pos = (current.pos[0] + move[0], current.pos[1] + move[1])
			if new_pos[0] > self.width - 1:
				continue
			if new_pos[0] < 0:
				continue
			if new_pos[1] > self.height - 1:
				continue
			if new_pos[1] < 0:
				continue
			if self.maze[new_pos[1]][new_pos[0]] != '#':
				node = Node(new_pos, current)
				node.G = node.parent.G + 1
				adj.append(node)

		return adj

	def get_F_value(self, node):
		H = self.manhattan_distance(node, self.end)
		F = node.G + H
		return F

	def astar(self):
		closed = []
		todo = [self.start]

		while True:
			current = todo.pop()
			closed.append(current)
			adjacents = self.get_adjacent(current)
			for adj in adjacents:
				for item in todo:
					if adj.pos == item.pos:
						if adj.G < item.G:
							item.G = adj.G
							item.parent = adj.parent
				else:
					todo.append(adj)
			if todo == []:
				return False
			if current.pos == self.end.pos:
				closed = sorted(closed, key=lambda n : self.get_F_value(n))
				break
			todo = sorted(todo, key=lambda n : self.get_F_value(n), reverse=True)

		step = closed[-1]
		path = [step.pos]
		while step.parent:
			path.append(step.parent.pos)
			step = step.parent

		# print path
		return path


	def print_path(self):
		path = sorted(self.astar(), key=lambda p : p[0], reverse=True)
		path = sorted(path, key=lambda p : p[1], reverse=True)
		print path
		if path:
			step = path.pop()
		else:
			step = None
		for y in range(len(self.maze)):
			for x in range(len(self.maze[y])):
				if (x, y) == step:
					print '*',
					if path:
						step = path.pop()
				else:
					print self.maze[y][x],
			print '\n',	

m = Maze(maze)
print m.start.pos, m.end.pos
m.print_path()