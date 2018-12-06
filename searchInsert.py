class Solution:
    def searchInsert(self, nums, target):
        """
        给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
        1.判断 target是否在nums里
        2.如果不在，插入
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # if target in nums:
        #     return nums.index(target)
        flag = True
        start_index = 0
        end_index = len(nums) - 1
        mid_index = (start_index + end_index) // 2
        while flag:
            if nums[mid_index] == target:
                return mid_index
            if start_index >= len(nums):
                return start_index
            if start_index > end_index:
                flag = False
            mid_index = (start_index + end_index) // 2
            if nums[mid_index] > target:
                end_index = mid_index - 1
            if nums[mid_index] < target:
                start_index = mid_index + 1

        if nums[start_index] < target:
            return start_index + 1
        return start_index


class Solution1:
    def searchInsert(self, nums, target):
        """
        给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
        1.判断 target是否在nums里
        2.如果不在，插入
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            return nums.index(target)
        for index, value in enumerate(nums):
            if value > target:
                nums.insert(index, target)
                return index
            index += 1
            if index == len(nums):
                nums.append(target)
                return index


if __name__ == '__main__':
    import_x = [1]
    solution = Solution()
    print(solution.searchInsert(import_x, 0))
