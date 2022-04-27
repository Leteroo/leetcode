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
    # preorder
    def tree(self, node):
        if not node:
            self.lis.append(-1)
            return
        self.lis.append(node.val)
        self.tree(node.left)
        self.tree(node.right)
# better method (inspired by #101)
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def equa(l, r):
            if l == None and r != None or  l != None and r == None:
                return False
            elif l == None and r == None:
                return True
            elif l.val != r.val:
                return False
            else:
                return equa(l.left, r.left) and equa(l.right, r.right)
        return equa(p, q)

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
# better method
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isSymm(l,r):
            if l == None and r != None or l != None and r == None:
                return False
            elif l == None and r == None:
                return True
            elif l.val != r.val:
                return False
            else:
                return isSymm(l.left,r.right) and isSymm(l.right,r.left)
        return isSymm(root.left,root.right)