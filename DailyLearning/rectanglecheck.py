#For a given 2d bitmap, find out the end points of a region that has only 1s and return true if those end points form a rectangle.
matrix = [[1,1,1,1,1],
          [1,0,0,0,1],
          [1,0,0,0,1],
          [1,0,0,0,1],
          [1,1,1,1,1]]


def rectanglecheck(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    result = []
    for i in range(4):
        result.extend(matrix.pop(0))
        matrix = list(zip(*matrix))[::-1]   
    #print (result)
    
    result2 = []
    while matrix:
        result2.extend(matrix.pop(0))
        matrix = list(zip(*matrix))[::-1]   
    #print (result2)    
    
    if 0 in result:
      return "This is not a rectangle"
    elif 1 in result2:
      return "This is not a rectangle"
    else:
      return "True!, This is a rectangle"

print (rectanglecheck(matrix))
