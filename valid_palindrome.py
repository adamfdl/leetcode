
def isPalindrome(s):

	# Clean the string first
	cleaned_string = ""
	for char in s:
		if char.isalnum():
			cleaned_string += char.lower()

	left = 0
	right = len(cleaned_string)-1

	i = 0
	# We need to check left <= right, so that 
	# we can check the character in the middle
	while left <= right:
		a = cleaned_string[left]
		b = cleaned_string[right]
		if a == b:
			left += 1
			right -= 1
			i += 1
		else:
			return False

	return True

x = isPalindrome("A man, a plan, a canal: Panama")
print(x)