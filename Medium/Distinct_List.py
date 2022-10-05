Distinct List
#Have the function DistinctList(arr) take the array of numbers stored in arr and determine the total number of duplicate entries. For example if the input is [1, 2, 2, 2, 3] then your program should output 2 because there are two duplicates of one of the elements.
Examples
Input: [0,-2,-2,5,5,5]
Output: 3
Input: [100,2,101,4]
#Output: 0



def DistinctList(arr):
  count=0
  for i in range(0,(len(arr)-1),1):
    if arr[i] == arr[i+1]:
      count += 1
    else:
      count = count
  return count

# keep this function call here 
print DistinctList(raw_input())
