# PYTHON3撰寫，easy mode
# 1. Two Sum，和數
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 固定第i+1個的數，與後面的數逐個相加，判斷有沒有等於target
        for i in range(len(nums)):  
            for j in range(i+1, len(nums)):    
                if nums[i] + nums[j] == target:     
                    if i != j:
                        return [i, j]
        return []
    # best solution
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 利用hash_table暫存nums串列內 數值和其所對應的索引值
        hash_table = {}     
        for i, num in enumerate(nums):      # enumerate(iterable, [start=0])：用於可迭代資料型態，傳回index與value
            if target - num in hash_table:
                return([hash_table[target - num], i])
            hash_table[num] = i             # 邊判斷邊建立hash_table
        return([])
        
# 9. Palindrome Number，判斷迴文數
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        strx = str(x)       # 將x轉成字串
        for i in range(len(strx)):
            if strx[i] != strx[-(i+1)]:     # 判斷由左數來和由右數來第i+1位的數有沒有相等
                return False
        return True
    # best solution
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        reversenum = 0
        temp_x = x
        while temp_x > 0:   # 將x反轉
            reversenum = reversenum * 10 + temp_x % 10    
            temp_x = temp_x // 10
        if reversenum != x:
            return False
        return True
        
# 13. Roman to Integer，羅馬數字符號轉十進位
class Solution:
    def romanToInt(self, s: str) -> int:
        al = ('I V X L C D M Q W E R T Y').split(' ')
        nu = [1, 5, 10, 50, 100, 500, 1000, 4, 9, 40, 90, 400, 900]
        table = {}
        for i in range(len(al)):
            table[al[i]] = nu[i]
        if 'CM' in s:
            s = s.replace('CM', 'Y')
        if 'CD' in s:
            s = s.replace('CD', 'T')
        if 'XC' in s:
            s = s.replace('XC', 'R')
        if 'XL' in s:
            s = s.replace('XL', 'E')
        if 'IX' in s:
            s = s.replace('IX', 'W')
        if 'IV' in s:
            s = s.replace('IV', 'Q')
        sum = 0
        for i in range(len(s)):
            sum += table[s[i]]
        return sum
        
# 14. Longest Common Prefix，若串列的字串有相同的前綴，輸出該前綴，沒有則輸出空字串
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        loop = 1000
        tempstr = ''
        a = strs[0]     # 將第一項當基準
        for i in strs:
            if len(i) < loop:
                loop = len(i)       # 找出最短元素的長度
        for i in range(loop):       # 比較 第一項與第j項 元素的第i+1個字母
            for j in range(len(strs)):
                if j != 0:          # 只比較第2項之後的元素
                    b = strs[j]
                    if a[i] != b[i]:    
                        return tempstr
            tempstr += a[i]
        return tempstr
        
# 20. Valid Parentheses，是否為有效的括號字串
class Solution:
    def isValid(self, s: str) -> bool:
        while '()' in s or '[]' in s or '{}' in s:
            s = s.replace('()', '')
            s = s.replace('[]', '')
            s = s.replace('{}', '')
        if s == '':
            return True
        else:
            return False
           
# 21. Merge Two Sorted Lists，merge並sort(小到大)兩個(singly)linked-list
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dum = ListNode(None)    # 值為None、指標只指向第一個節點的旁觀節點
        prev = dum              # 設定prev節點，負責移動指標接取next
        while list1 and list2:      # 判斷list1 & list2是否皆有值
            if list1.val <= list2.val:  # 比較list1 & list2 第一個節點的值
                prev.next = list1       # prev的指標指向值最小的節點
                list1 = list1.next      # 第一個節點的值比較小的list，指標向後移1位
            else:
                prev.next = list2
                list2 = list2.next
            prev = prev.next            # prev指標向後移1位，準備接取下一個節點
        if list1 == None:
            prev.next = list2
        elif list2 == None:
            prev.next = list1
        return dum.next
        
# 26. Remove Duplicates from Sorted Array，若陣列內有值重複的項，保留一項並刪除其他項，傳回非重複項的總數，且計算後原輸入陣
#     列大小不變，以'_'補足項數
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:    # 是否為空陣列
            print('nums=', nums)
            return 0
        big = max(nums) + 1     # 用來取代重複項的值，設定為陣列最大值+1以利後續的排序。
        times = len(nums)
        for i in range(times):
            if i != 0:
                if nums[i] == nums[i - 1]:  # 判斷前一項與當前項的值是否相同
                    nums[i - 1] = big       # 將前一項的值改成big
        k = times - nums.count(big)         # 陣列總數減去big的數，即非重複項的總數
        nums.sort()                         # 由小到大排序
        for i in range(times):
            if nums[i] == big:
                nums[i] = '_'               # 將big取代成'_'，滿足題目需求
        print('nums=', nums)
        return k
        
# 27. Remove Element，給定一個整數，將陣列內與該數相同的項刪除，傳回不同項的總數，且計算後原輸入陣列大小不變，以'_'補足項數
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:    
            print('nums=', nums)
            return 0
        big = max(nums) + 1     
        times = len(nums)
        for i in range(times):
            if nums[i] == val:
                nums[i] = big
        k = times - nums.count(big)         
        nums.sort()                         
        for i in range(times):
            if nums[i] == big:
                nums[i] = '_'               
        print('nums=', nums)
        return k
        
# 28. Implement strStr()，已知變數 needle、hashstack 2個字串，判斷needle是否存在於hashstack裡，並傳回最小索引值
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:      # needle為空字串傳回0
            return 0
        if needle in haystack:
            ind = haystack.find(needle)
            return ind
        return -1           # 不包含傳回-1
        
# 35. Search Insert Position，已知1個元素為正整數且由小到大排列的陣列，輸入1個正整數，找出該正整數在陣列內的索引值，或插入陣
#     列後該整數的索引值
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
    # 時間複雜度必須為O(log2(n))->使用二分法
        mn = 0
        mx = len(nums) - 1
        while mn <= mx:
            mid = (mn+mx) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                mx = mid - 1
            if nums[mid] < target:
                mn = mid + 1
        return mn
        
# 53. Maximum Subarray，已知1個元素為整數的陣列，尋找最大子陣列的和，且該子陣列的元素必須為連續不間斷的
class Solution:     # 動態規劃法
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]     
        localmax = 0
        globalmax = -10**4
        for i in range(len(nums)):
            localmax = max(nums[i],nums[i]+localmax)
            if localmax > globalmax:
                globalmax = localmax
        return globalmax
        
# 58. Length of Last Word，已知一字串，單字間只有空白分隔，傳回該字串最後一個單字的長度(不含空白)
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip(' ')
        length = 0
        for i in range(len(s)):
            if s[-(i+1)] == ' ':
                break
            length += 1
        return length
        
# 66. Plus One，已知輸入為一個陣列，該陣列為將一個大正整數(不含有前導0)逐位分割而成，依照10進位制進行進位，傳回將最後一項+1的結果
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        local = digits
        numstr = ''
        for num in local:
            numstr += str(num)
        numstr = str(eval(numstr) + 1)
        local = [int(i) for i in numstr]
        return local

# 67. Add Binary，二進位加法，輸入為元素皆為1、0的2個字串(無前導0)，依照二進位將2字串相加並傳回字串
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        sumbin = str(eval(a) + eval(b))
        binarray = [int(i) for i in sumbin]
        output = ''
        for i in range(-1, -(len(sumbin)+1), -1):
            if i != -len(sumbin):
                if binarray[i] > 1:
                    binarray[i] -= 2
                    binarray[i-1] += 1
                    continue
            if binarray[i] > 1:
                binarray[i] = 10 + (binarray[i]-2)
        for i in binarray:
            output += str(i)
        return output
        
# 69. Sqrt(x)，找平方根，且無條件捨去小數部分
class Solution:
    def mySqrt(self, x: int) -> int:
        sqrt = int(pow(x, 0.5))
        return sqrt
