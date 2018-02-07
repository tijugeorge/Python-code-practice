

def revString(string):
  string = list(string)
  #print(string)
  l = 0
  r = len(string)-1
  mid = r//2
  #print(l, r, mid)
  #print(string[l], string[r])
  while (mid != l) and (mid != r):
    
    string[l], string[r] = string[r], string[l]
    l+=1
    r-=1
  return ("".join(string))
  
  
sent = "Keep in mind that both positive and negative testing is equally important for effective testing which help to improve quality of software. Negative testing help to find more defects & improve the quality of the software application under test but it should be done once the positive testing is completed. End users can enter any input values, such real life scenarios can be tested before moving software live. Main aim means purpose of Positive and Negative Testing is to prove that the application works as per the requirements and specifications"

print(revString(sent))

print("-"*80)
print(sent[::-1])
    
