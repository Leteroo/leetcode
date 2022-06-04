# 70. Climbing Stairs，爬樓梯
class Solution:
    def climbStairs(self, n: int) -> int:
        hash_table = {}
        hash_table[str(1)] = 1
        hash_table[str(2)] = 2     
        
        # N層樓梯的走法總數 = 第一步走1階的走法總數 + 第一步走2階的走法總數
        for i in range(1, n+1):
            if i > 2:
                hash_table[str(i)] = hash_table[str(i-1)] + hash_table[str(i-2)]
        method = hash_table[str(n)]
        return method

# 83. Remove Duplicates from Sorted List，已知一單向且sorted(小到大)的linked-list，刪除list內的重複項
class Solution:
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

# 94. Binary Tree Inorder Traversal，return Inorder Traversa of node values
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.res = []
        self.dfs(root)
        return self.res
    def dfs(self, node):
        if not node:
            return
        self.dfs(node.left)
        self.res.append(node.val)
        self.dfs(node.right)    

# 100. Same Tree，check if two binary trees are same or not
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.lis = []
        self.tree(p)
        a = self.lis
        
        self.lis = []
        self.tree(q)
        b = self.lis
        
        if a == b:
            return True
        return False
    def tree(self, node):
        if not node:
            self.lis.append(-1)
            return
        self.lis.append(node.val)
        self.tree(node.left)
        self.tree(node.right)
        
    # better solution (inspired by #101)
    """
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.equa(p, q)
        
    def equa(self, l, r):
        if l == None and r != None or  l != None and r == None:
            return False
        elif l == None and r == None:
            return True
        elif l.val != r.val:
            return False
        else:
            return self.equa(l.left, r.left) and self.equa(l.right, r.right)
    """
        
# 101. Symmetric Tree，check if a binary tree is symmetric around its center
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        self.lis = []
        self.treeleft(root)
        a = self.lis
        
        self.lis = []
        self.treeright(root)
        b = self.lis
        
        if a == b:
            return True
        return False
        
    def treeleft(self, node):
        if not node:
            self.lis.append(-1)
            return
        self.lis.append(node.val)
        self.treeleft(node.left)
        self.treeleft(node.right)
        
    def treeright(self, node):
        if not node:
            self.lis.append(-1)
            return
        self.lis.append(node.val)
        self.treeright(node.right)
        self.treeright(node.left)
        
    # better solution
    """
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isSymm(root.left,root.right)
        
    def isSymm(self, l, r):
        if l == None and r != None or l != None and r == None:
            return False
        elif l == None and r == None:
            return True
        elif l.val != r.val:
            return False
        else:
            return self.isSymm(l.left,r.right) and self.isSymm(l.right,r.left)   
    """

# 104. Maximum Depth of Binary Tree
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left)+1, self.maxDepth(root.right)+1)
        
# 168. Excel Sheet Column Title，given an integer，return its corresponding column title as it appears in an Excel sheet。
#      (A = 1 。。。 Z = 26、AA = 27 。。。)
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        table = {}
        sheet = []
        ot = ''
        for i in range(26):
            table[i] = chr(65+i)
            
        while columnNumber > 0:
            b = columnNumber - 1
            sheet.append(b % 26)
            if columnNumber <= 26:
                break
            columnNumber = b // 26
            
        for i in range(-1, -len(sheet)-1, -1):
            ot += table[sheet[i]]
        return ot

# 171. Excel Sheet Column Number，given a string(columnTitle)，return its corresponding column number in an Excel sheet
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        table = {}
        su = 0
        for i in range(1, 27):
            table[chr(64+i)] = i
        for i in range(-1, -len(columnTitle)-1, -1):
            su += table[columnTitle[i]] * pow(26, -i-1)
        return su
        
# 202. Happy number，replace the number by the sum of the squares of its digits，until the number equals 1, return True.
#      Or it loops endlessly in a cycle which does not include 1, return False
class Solution:
    def isHappy(self, n: int) -> bool:
        hash_table = {}
        i = 0
        
        while n != 1:
            sum = 0
            
            if n in hash_table:
                return False
            hash_table[n] = i
            i += 1
            
            while n >= 10:
                tempnum = n % 10
                sum += pow(tempnum, 2)
                n = n // 10
            sum += pow(n, 2)
            n = sum
            
        return True
        
# 231. Power of two，given an integer n, if n is power of two, return True. Otherwise, return False.
class Solution(object):
    def isPowerOfTwo(self, n):
        if n < 0:
            return False
        if n == 0:
            return False
        return not n & n - 1  
        
    #best solution
    """
    def isPowerOfTwo(self, n):
        return n and n & n - 1
    """
        
# 867. Transpose matrix
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])
        ans = [[None]*m for i in range(n)]
    
        for i in range(m):
            for j in range(n):
                ans[j][i] = matrix[i][j]
        
        return ans
    
    #best solution:
    """
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return [i for i in zip(*matrix)]
    """
        
# 111. Minimum Depth from root down to leaf of Binary Tree.
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        l_height = self.minDepth(root.left)
        r_height = self.minDepth(root.right)        
        if l_height == 0 or r_height == 0:
            return 1 + max(l_height, r_height)
        
        return 1 + min(l_height, r_height)
        
    # best solution
    """
from collections import deque

    def minDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0
        if not root: return depth
        queue = deque([root])
        while queue:
            depth += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                elif not node.left:
                    return depth
    """
