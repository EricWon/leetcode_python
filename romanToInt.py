class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roam_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000, "": 0}
        roam_str = s[::-1]
        # roam_str = s
        pre_str = ""
        counts = 0
        for str_t in roam_str:
            if str_t == "I":
                if pre_str == "V" or pre_str == "X":
                    pre_str = str_t
                    counts -= 1
                    continue
                counts += 1
                pre_str = str_t
                continue
            if str_t == "X":
                if pre_str == "L" or pre_str == "C":
                    pre_str = str_t
                    counts -= 10
                    continue
                counts += 10
                pre_str = str_t
                continue
            if str_t == "C":
                if pre_str == "D" or pre_str == "M":
                    pre_str = str_t
                    counts -= 100
                    continue
                counts += 100
                pre_str = str_t
                continue
            counts += roam_dict.get(str_t)
            pre_str = str_t
        return counts


if __name__ == '__main__':
    import_str = "MCMXCIV"
    solution = Solution()
    print(solution.romanToInt(import_str))
