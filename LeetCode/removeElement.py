class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if val not in nums:
            return len(nums)
        flag = val in nums
        nums_len = len(nums)
        index = nums.index(val, 0, nums_len)
        while flag:
            nums.append(nums.pop(index))
            nums_len -= 1
            flag = val in nums[0:nums_len]
            if flag:
                index = nums[0:nums_len].index(val)
        return nums_len


if __name__ == '__main__':
    import_x = [1]
    solution = Solution()
    print(solution.removeElement(import_x, 1))
    print(import_x)
