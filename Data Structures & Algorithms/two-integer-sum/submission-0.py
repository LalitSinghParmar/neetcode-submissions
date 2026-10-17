class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp_dict = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in temp_dict:
                return [temp_dict[diff], i]
            temp_dict[nums[i]] = i
            