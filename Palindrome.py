class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return x >= 0 and str(x) == str(x)[::-1]
        # if x < 0:
        #     return False
        # if x < 10:
        #     return True
        #
        # str_x = str(x)
        # if len(str_x) == 1:
        #     return True
        # for i in range(len(str_x) - 1):
        #     if i > len(str_x) / 2:
        #         return True
        #     if str_x[i] != str_x[-1 - i]:
        #         return False
        # return True


if __name__ == '__main__':
    import_x = 12321
    solution = Solution()
    print(solution.isPalindrome(import_x))
