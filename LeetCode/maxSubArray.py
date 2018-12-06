class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        max_list = []
        max_sum = 0
        temp_list = []
        temp_sum = 0
        for number in nums:
            if temp_sum + number < 0:
                temp_sum = 0
                temp_list = []
                continue
            temp_sum += number
            temp_list.append(number)
            if temp_sum > max_sum:
                max_list = []
                max_list.extend(temp_list)
                max_sum = temp_sum
                continue
        print(max_list)
        return max_sum


if __name__ == '__main__':
    import_x = [-2, -1]
    solution = Solution()
    print(solution.maxSubArray(import_x))
