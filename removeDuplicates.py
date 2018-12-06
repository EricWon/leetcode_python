class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return nums
        list_len = len(nums)
        index = 1
        pre_num = nums[0]
        while index < list_len:
            if pre_num == nums[index]:
                nums.append(nums.pop(index))
                list_len -= 1
                continue
            pre_num = nums[index]
            index += 1
        return index


if __name__ == '__main__':
    import_x = [1, 1, 2, 2, 2, 2, 4, 5, 6, 6, 6, 6, 7]
    solution = Solution()
    print(solution.removeDuplicates(import_x))
    print(import_x)
