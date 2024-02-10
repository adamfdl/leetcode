def isValid(s):
  
  if len(s) % 2 != 0:
    return False
  
  openBrackets = ["(", "{", "["]
  
  hash = {
    "}": "{",
    "]": "[",
    ")": "("
  }
  
  stack = []
  for char in s:
    
    # If char in open brackets, append
    if char in openBrackets:
      stack.append(char)
      continue
    
    # If stack is not empty
    # If top of stack matches the closing bracket, pop
    # If not, we return false
    if len(stack) != 0 and stack[-1] == hash[char]:
      stack.pop()
    else:
      return False
  
  return len(stack) == 0


x = isValid("([}}])")
print(x)