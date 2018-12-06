class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        count = 0
        nums = "1"
        while count < n - 1:
            index = 0
            pre_str = nums[0]
            flag_index = 0
            current_nums = ""
            for key, value in enumerate(nums):
                if pre_str != value and index != 0:
                    current_nums += (str(index) + pre_str)
                    pre_str = value
                    index = 0
                if pre_str == value:
                    index += 1
                flag_index += 1
                if flag_index == len(nums):
                    current_nums += (str(index) + pre_str)
                    break
            count += 1
            nums = current_nums
        return nums


if __name__ == '__main__':
    solution = Solution()
    print(solution.countAndSay(6))
