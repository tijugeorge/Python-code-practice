#Sort restaurants by their number of reviews

import collections

def reviews(restaurants):
  storage = {}
  for restaurant in restaurants:
    if restaurant in storage:
      storage[restaurant] += 1
    else:
      storage[restaurant] = 1
  storage = collections.Counter.most_common(storage)
  return storage[0][0]
      
      
      
restaurants = ['A','A','D','C','F','G','T','R','R','D','S','A','W','E','S','D','F','C','V','G','R','E','W','S','S','F','W','S','X','C','R','E','S','X','C','V','D']

print(reviews(restaurants))
    
