class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        str_list = []
        left_brackets = ['(', '{', '[']
        right_brackets = [')', '}', ']']
        combination_list = ['()', '[]', '{}']
        for strs in s:
            if strs in left_brackets:
                str_list.insert(0, strs)
                continue
            if strs in right_brackets:
                if len(str_list) == 0:
                    return False
                list_str = str_list.pop(0)
                if list_str + strs not in combination_list:
                    return False
        if len(str_list)>0:
            return False
        return True


if __name__ == '__main__':
    import_x = "([])"
    solution = Solution()
    print(solution.isValid(import_x))
