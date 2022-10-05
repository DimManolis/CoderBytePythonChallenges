#Consonant Count
#Have the function ConsonantCount(str) take the str string parameter being passed and return the number of consonants the string contains.
#Examples
#Input: "Hello World"
#Output: 7
#Input: "Alphabets"
#Output: 6

def ConsonantCount(strParam):
  # code goes here
  cons = ['z','x','c','v','b','n','m','s','d','f','g','h','j','k','l','q','w','r','t','y','p']
  s = strParam.lower()
  c_counter = 0
  for x in s:
   if x in cons:
     c_counter += 1
  
  return c_counter

# keep this function call here 
print ConsonantCount(raw_input())
