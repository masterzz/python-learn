# 1、合并两个有序数组
from typing import List, Optional


class ListNode:
    pass


class Solution:
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
    n1 = [1,2,3,0,0,0]
    n2 = [2,5,6]
    a = Solution()
    a.merge(nums1=n1,m=1,nums2=n2,n=2)


