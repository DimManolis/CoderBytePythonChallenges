## Have the function NumberReverse(str) take the str parameter being passed which will be a string of numbers, and return a new string with the numbers in reverse order.
##Examples
##Input: "1 2 3"
##Output: 3 2 1
#Input: "10 20 50"
#Output: 50 20 10##
  
def NumberReverse(strParam):

  return " ".join(reversed(strParam.split(" ")))
# keep this function call here 
print NumberReverse(raw_input())
