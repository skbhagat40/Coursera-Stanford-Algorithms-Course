current_level = [[A]
next_level = deque()
paths = []
while current_level:
	node = current_level.pop()
	if node == p or node == q:
		ans.apend(current_level)
	next_level.extend([node.left, node.right])
	if not current_level:
		if next_level:
			current_level = next_level

for a,b in zip(reversed(path[0]),reversed(path[1])):
	if a == b:
		return a

def traverse(root, path):
	if root.val == p:
		return path
	else:
		path.append(root)
		traverese(root.left)
		traverse(root.right)

def time(root, step):
	root.intime = step
	l = time(root.left, step +1)
	r = time(root.right, step + 2)
	root.outtime = step

def invert(root):
	l = invert(root.left)
	r = invert(root.right)
	root.left = r
	root.right = l
	return root

def ll(root, ll_root):
	if root is None:
		return
	ll_root.next = root
	ll(root.left, ll_root.next)
	ll(root.right, ll_root.next)


	
