def zigzagLevelOrder(self, root):
    solution = []
    thisLevel =[]
    if root != None:
        thisLevel.append(root)
    leftToRight = True
    while len(thisLevel)>0:
        levelSolution = []
        nextLevel = []
        while len(thisLevel)>0:
            node = thisLevel.pop()
            levelSolution.append(node.val)
            if leftToRight:
                if node.left != None:
                    nextLevel.append(node.left)
                if node.right != None:
                    nextLevel.append(node.right)
            else:
                if node.right != None:
                    nextLevel.append(node.right)
                if node.left != None:
                    nextLevel.append(node.left)
        thisLevel = nextLevel
        solution.append(levelSolution)
        leftToRight = not leftToRight
    return solution
