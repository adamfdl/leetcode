def search(nums, target):
  left = 0
  right = len(nums) -1
  
  # Why left <= right? Because if the loop kept on going
  # until left has passed right, then that means we have not 
  # found the target we are looking for
  while left <= right:

    # Double slash in python means divide and round to the nearest
    # whole integer. Ex 10 // 3 equals 3
    m = (left + right) // 2
    
    # If number in 'm' is bigger than the target,
    # We are going to start searching from l ~ r=m-1.
    # Meaning we are going to search the value to the left (shrinking to left)
    if nums[m] > target:
      right = m -1
    
    # If number in 'm' is smaller than the target,
    # We are going to start searching from l=m+1 ~ r
    # Meaning we are going to search the value to the right (shrinking to right)
    elif nums[m] < target:
      left = m + 1
    
    # If we get here, it means that nums[m] equals to the target
    # And we can return the index
    else:
      return m
      
  
  return -1
      