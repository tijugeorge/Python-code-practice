#Given an array of numbers, return the mode—the number that appears the most times.
#https://insights.dice.com/2015/11/06/the-trick-to-coding-interview-questions/


def get_mode_brute_force(nums): #gives O(n^2)
  mode = None
  max_count = 0
  for potential_mode in nums:
    count = 0
    for num in nums:
      if num == potential_mode:
        count+=1
    if count > max_count:
      max_count = count
      mode = potential_mode
  return mode
  
  
nums = [1,2,2,3,3,3,4,5,6,7,3,2,4,5,6,7]

print(get_mode_brute_force(nums))

#solution 2 : Sorting
nums = [1,2,2,3,3,3,4,5,6,7,3,2,4,5,6,7]
def get_mode_sorting(nums): # gives O(nlogn) as to sort it takes nlogn
  if len(nums) == 0:
    return None
  elif len(nums) == 1:
    return nums[0]
   
  sorted_nums = sorted(nums)
  
  mode, previous_num = None, None
  max_count, current_count = 0,0
  for current_num in sorted_nums:
    if current_num == previous_num:
      current_count+=1
    if current_count > max_count:
      max_count = current_count
      mode = current_num
    if current_num!=previous_num:
      current_count = 1
    previous_num = current_num
  
  return mode
  
print(get_mode_sorting(nums))


def get_mode_hashing(nums):#takes O(n) as using dictionary property of O(1) to insertions and look up
  counts = {}
  for num in nums:
    if num in counts:
      counts[num] += 1
    else:
      counts[num] = 1
  max_count = 0
  print(counts)
  for num, count in counts.items():
    if count > max_count:
      max_count = count
      mode = num
  return mode
  
print(get_mode_hashing(nums))   
    
    
    
