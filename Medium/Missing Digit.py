Missing Digit
#Have the function MissingDigit(str) take the str parameter, which will be a simple mathematical formula with three numbers, a single operator (+, -, *, or /) and an equal sign (=) and return the digit that completes the equation. In one of the numbers in the equation, there will be an x character, and your program should determine what digit is missing. For example, if str is "3x + 12 = 46" then your program should output 4. The x character can appear in any of the three numbers and all three numbers will be greater than or equal to 0 and less than or equal to 1000000.
Examples
Input: "4 - 2 = x"
Output: 2
Input: "1x0 * 12 = 1200"
#Output: 0


def MissingDigit(strParam):
  
  l=list(strParam.split())
  first_op = l[0]
  operator = l[1]
  second_op = l[2]
  result = l[-1]
  if 'x'  in result:
    x = result
    first_num = int(first_op)
    second_num = int(second_op)

    if operator == '+':
      s = first_num + second_num
    elif operator == '-' :
      s = first_num - second_num
    elif operator == '*' :
      s = first_num * second_num
    elif operator == '/' :
      s = first_num // second_num
  else : 
    result = int(result)

    if 'x' in first_op :
      x = first_op
      second_num = int(second_op)

      if operator == '+':
        s = result - second_num
      elif operator == '-' :
        s = result + second_num
      elif operator == '*' :
        s = result // second_num
      elif operator == '/' :
        s = result * second_num

    else :
      x = second_op
      first_num = int(first_op)
      
      if operator == '+':
        s = result - first_num
      elif operator == '-' :
        s = first_num - result
      elif operator == '*' :
        s = result // first_num
      elif operator == '/' :
        s = first_num // result
  s = str(s)
  key = 0
  for i in x :
    if i == 'x':
      final = s[key]
    else:
      key+= 1
  return final

# keep this function call here 
print MissingDigit(raw_input())
