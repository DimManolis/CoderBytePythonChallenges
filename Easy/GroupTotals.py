#Group Totals
Have the function GroupTotals(strArr) read in the strArr parameter containing key:value pairs where the key is a string and the value is an integer. Your program should return a string with new key:value pairs separated by a comma such that each key appears only once with the total values summed up.

For example: if strArr is ["B:-1", "A:1", "B:3", "A:5"] then your program should return the string A:6,B:2.

Your final output string should return the keys in alphabetical order. Exclude keys that have a value of 0 after being summed up.
Examples
Input: ["X:-1", "Y:1", "X:-4", "B:3", "X:5"]
Output: B:3,Y:1
Input: ["Z:0", "A:-1"]
#Output: A:-1


def GroupTotals(strArr):
  items_0 = [s.split(':') for s in strArr]
  items = [[item[0] , int(item[1])] for item in items_0]
  d = {}
  for row in items:
    if row[0] not in d :
      d[row[0]]=[]
    d[row[0]].append(row[1:])
  for key in d:
    d[key] = [sum(x) for x in zip(*d[key])]
  
  d = {k:v for k,v in d.items() if v!=[0]}
  return ",".join(str(k)+":"+str(*d[k]) for k in sorted(d))
  
  
print GroupTotals(raw_input())
