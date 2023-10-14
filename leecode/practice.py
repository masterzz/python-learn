# 1、合并两个有序数组
from typing import List, Optional


class ListNode:
    pass







class Solution:
    """
    1.两数之和
    给定一个整数数组nums和一个整数目标值target，请你在该数组中找出和为目标值target
    的那两个整数，并返回它们的数组下标。
    你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
    你可以按任意顺序返回答案。
    """

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)
        result  = []
        for i in range(l):
            for j in range(i+1,l):
                if nums[i] +nums[j] == target:
                    result.append(i)
                    result.append(j)
        return result

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1
        in-place instead.
        1、全部元素先加进来
        2、单个非递减顺序排列，用冒泡
        3、两个非递减排序
        """
        temp = []
        for i in nums1:
            # if cursor is None or cursor <=i :
            temp.append(i)
        for j in nums2:
            temp.append(j)
        l = len(temp)
        for i in range(l):
            for j in range(l):
                pass
        print(temp)

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        pass

if __name__ == '__main__':
    # nums = [2,7,11,15]
    # target = 9
    a = Solution()
    nums = [3, 2, 4]
    target = 6
    solution = a.twoSum(nums = nums,target = 6)
    print(solution)


