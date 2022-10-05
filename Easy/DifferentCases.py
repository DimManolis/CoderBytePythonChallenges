#Different Cases
#Have the function DifferentCases(str) take the str parameter being passed and return it in upper camel case format where the first letter of each word is capitalized. The string will only contain letters and some combination of delimiter punctuation characters separating each word.

#For example: if str is "Daniel LikeS-coding" then your program should return the string DanielLikesCoding.
Examples
#Input: "cats AND*Dogs-are Awesome"
#Output: CatsAndDogsAreAwesome
#Input: "a b c d-e-f%g"
#Output: ABCDEFG

def DifferentCases(strParam):
 s = ''
 l = []
 
 for ch in strParam:
    if ch.isalpha() :
      s += ch
    else :
      s += ' '
 
 for word in s.split():
   word = word.capitalize()
   l.append(word)
 return ''.join(l)
  # keep this function call here 
print DifferentCases(raw_input())
