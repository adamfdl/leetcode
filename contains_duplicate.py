def containsDuplicate(nums):
    x = {}
    for num in nums:
        if num in x:
            return True
        else: 
            x[num] = True
    return False

x = containsDuplicate([3,3])
print(x)