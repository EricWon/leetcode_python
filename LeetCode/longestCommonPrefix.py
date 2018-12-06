class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        first_strs = strs[0]
        first_len = len(first_strs)
        commonPrefix = ""
        for i in range(first_len):
            for str_t in strs:
                if i == len(str_t):
                    return commonPrefix
                if str_t[i] != first_strs[i]:
                    return commonPrefix
            commonPrefix += first_strs[i]
        return commonPrefix


if __name__ == '__main__':
    import_x = ["flower","flow","flight"]
    solution = Solution()
    print(solution.longestCommonPrefix(import_x))
