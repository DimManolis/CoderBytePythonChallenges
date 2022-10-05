K Unique Characters
#Have the function KUniqueCharacters(str) take the str parameter being passed and find the longest substring that contains k unique characters, where k will be the first character from the string. The substring will start from the second position in the string because the first character will be the integer k. For example: if str is "2aabbacbaa" there are several substrings that all contain 2 unique characters, namely: ["aabba", "ac", "cb", "ba"], but your program should return "aabba" because it is the longest substring. If there are multiple longest substrings, then return the first substring encountered with the longest length. k will range from 1 to 6.
Examples
Input: "3aabacbebebe"
Output: cbebebe
Input: "2aabbcbbbadef"
#Output: bbcbbb

def KUniqueCharacters(strParam):
  k=int(strParam[0])
  temp_string = string = strParam[1:k+1]
  window = k
  while window < len(strParam) - 1:
    if len(set(temp_string)) <= k:
      if len(temp_string) > len(string):
        string = temp_string
      window+= 1
      temp_string += strParam[window]
    else:
      temp_string = temp_string[1:len(temp_string)]
  if len(temp_string) > len(string):
    string = temp_string

  return string


# keep this function call here 
print KUniqueCharacters(raw_input())
