# Naive solution O(n2)
# Space complexity O(1)
def twoSum(nums, target): 
  for i in range(len(nums)):
    for j in range(len(nums)):
      if i == j:
        continue
      num1 = nums[i]
      num2 = nums[j]
      if (num1 + num2) == target:
        return [i, j]

# Time complexity O(n)
# Space complexity O(n)
def twoSumHashmap(nums, target):
  hash_map = {}
  for i in range(len(nums)):
    if nums[i] in hash_map:
      return [i, hash_map[nums[i]]]
    else:
      hash_map[target - nums[i]] = i

# x = twoSum([2,7,11,15], 9)

x = twoSumHashmap([1,3, 5], 6)
print(x)