#FizzBuzz
#Have the function FizzBuzz(num) take the num parameter being passed and return all the numbers from 1 to num separated by spaces, but replace every number that is divisible by 3 with the word "Fizz", replace every number that is divisible by 5 with the word "Buzz", and every number that is divisible by both 3 and 5 with the word "FizzBuzz". For example: if num is 16, then your program should return the string "1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz 16". The input will be within the range 1 - 50.
#Examples
#Input: 3
#Output: 1 2 Fizz
#Input: 8
#Output: 1 2 Fizz 4 Buzz Fizz 7 8

def FizzBuzz(n):
 s=''
 for i in range(1, n+1):
   if i % 3 == 0 and i % 5 == 0:
     s+=' ' + "FizzBuzz"
   elif i % 3 == 0:
     s+=' ' + "Fizz"
   elif i % 5 == 0:
     s+=' ' + "Buzz"
   else:
     s+=' ' + str(i)
     
 return s
    
# keep this function call here 
print FizzBuzz(raw_input())
