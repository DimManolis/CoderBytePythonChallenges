Formatted Division
#Have the function FormattedDivision(num1,num2) take both parameters being passed, divide num1 by num2, and return the result as a string with properly formatted commas and 4 significant digits after the decimal place. For example: if num1 is 123456789 and num2 is 10000 the output should be "12,345.6789". The output must contain a number in the one's place even if it is a zero.
Examples
Input: 2 & num2 = 3
Output: 0.6667
Input: 10 & num2 = 10
#Output: 1.0000



def FormattedDivision(num1,num2):
  result = "%.4f"%(float(num1)/ num2)


  # code goes here
  return "{:,}".format(float(result))
# keep this function call here 
print FormattedDivision(raw_input())
