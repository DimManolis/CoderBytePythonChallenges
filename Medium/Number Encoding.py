Number Encoding
#Have the function NumberEncoding(str) take the str parameter and encode the message according to the following rule: encode every letter into its corresponding numbered position in the alphabet. Symbols and spaces will also be used in the input. For example: if str is "af5c a#!" then your program should return 1653 1#!.
Examples
Input: "hello 45"
Output: 85121215 45
Input: "jaj-a"
#Output: 10110-1



def NumberEncoding(strParam):
  string = strParam.lower()
  d=""
  for ch in string :
    if ch.isalpha():
      n = ord(ch) -96
      d += str(n)
    else:
      n = ch
      d += n
  return d
# keep this function call here 
print NumberEncoding(raw_input())
