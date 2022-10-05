Equivalent Keypresses
Have the function EquivalentKeypresses(strArr) read the array of strings stored in strArr which will contain 2 strings representing 
two comma separated lists of keypresses. Your goal is to return the string true if the keypresses produce the same printable string 
and the string false if they do not. A keypress can be either a printable character or a backspace represented by -B. 
You can produce a printable string from such a string of keypresses by having backspaces erase one preceding character.

#Examples
#Input: ["a,b,c,d", "a,b,c,d,-B,d"]
#Output: true
#Input: ["c,a,r,d", "c,a,-B,r,d"]
#Output: false

def EquivalentKeypresses(strArr):
 words = []
 for i in strArr :
   s = ""
   i = i.replace("," , "")
   i = i.replace("-B" , "1")
   for n in i:
     if n == "1" :
       s = s[:-1]
     else :
       s += n
   words.append(s)
 if words[0] == words[1] :
    return "true"
 else :
     return "false"

# keep this function call here 
print EquivalentKeypresses(raw_input())
