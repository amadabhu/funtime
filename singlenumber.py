class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        nums_set = set(nums)
        nums_set = list(nums_set)
        nums_dict = {}
        for i in nums_set:
            nums_dict[i] = None

        keyz = nums_dict.keys()

        for key in keyz:
            value_count = nums.count(key)
            nums_dict[key] = value_count
            if value_count == 1:
                return key 
            else:
                continue
