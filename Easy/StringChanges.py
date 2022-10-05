#String Changes
#Have the function StringChanges(str) take the str parameter being passed, which will be a string containing letters from the alphabet, and return a new string based on the following rules. Whenever a capital M is encountered, duplicate the previous character (then remove the M), and whenever a capital N is encountered remove the next character from the string (then remove the N). All other characters in the string will be lowercase letters. For example: "abcNdgM" should return "abcgg". The final string will never be empty.
#Examples
#Input: "MrtyNNgMM"
#Output: rtyggg
#Input: "oMoMkkNrrN"
#Output: ooookkr

def StringChanges(strParam):
  rl=''
  for char in strParam:
    if rl and rl[-1] == 'N':
      rl = rl[:-1]
      continue
    if char == 'M':
      if rl:
        rl += rl[-1]
      continue
    rl += char
  rl = rl.strip('N')

  return rl


# keep this function call here 
print StringChanges(raw_input())
