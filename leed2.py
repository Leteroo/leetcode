# 70. Climbing Stairs，爬樓梯
class Solution:
    def climbStairs(self, n: int) -> int:
        hash_table = {}
        hash_table[str(1)] = 1
        hash_table[str(2)] = 2         # N層樓梯的走法總數 = 第一步走1階的走法總數 + 第一步走2階的走法總數
        for i in range(1, n+1):
            if i > 2:
                hash_table[str(i)] = hash_table[str(i-1)] + hash_table[str(i-2)]
        method = hash_table[str(n)]
        return method

# 83. Remove Duplicates from Sorted List，已知一單向且sorted(小到大)的linked-list，刪除list內的重複項
class Solution:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        watch = ListNode(None)
        point = watch
        
        if not head:
            return watch.next
        
        while head:
            if head.val == point.val:
                head = head.next
                continue
            point.next = head
            head = head.next
            point = point.next
            
        point.next = None
            
        return watch.next

# 88. Merge Sorted Array，已知兩sorted(小到大)整數陣列，merge兩陣列後sort(小到大)指派給nums1(長度為m+n)，m為nums1長度，
#     n為nums1陣列尾端0的個數以及nums2的長度，該函式輸出為None
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if not nums2:
            return
        if not nums1:
            for i in range(n):
                nums1[i] = nums2[i]
                return
        nums1.extend(nums2)
        nums1.sort()
        for i in range(n):
            nums1.remove(0)
  
# Q19，
      