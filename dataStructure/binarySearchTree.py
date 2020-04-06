#genrate different form of tree
# Binary Tree Node
class newNode:
	# initailize variables
	def __init__(self, item):
		self.key=item
		self.left = None
		self.right = None

# method to traverse list  in preorder manner i.e , RLR
def preorder(root) :

	if (root != None) :
		print(root.key, end = " " )
		preorder(root.left)
		preorder(root.right)
	
# function for constructing trees
def createTree(start, end):
    #initialize list
	list = []
    #chedk if start > end then return empty list
	if (start > end) : 	
		list.append(None)
		return list
	
	for i in range(start, end + 1):
        #generate lef subTree
		leftTree = createTree(start, i - 1)
        #generate right subTree
		rightTree = createTree(i + 1, end)
        #enter elements in right or left subtree
		for j in range(len(leftTree)) :
			left = leftTree[j]
			for k in range(len(rightTree)):
				right = rightTree[k]
                #concate two tree into a main tree whose root is i
				node = newNode(i)
				node.left = left
				node.right = right
                #append nodes into list
				list.append(node)
	return list


# Construct all possible BSTs
totalTree = createTree(1, 3)
print("Preorder traversals of constructed BSTs are")
for i in range(len(totalTree)):
    preorder(totalTree[i])
    print()