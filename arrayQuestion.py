from answers import arrayAnswers as arrAnswers

# These questions comes from [https://algomap.io/]
# Feel free to add more TEST CASES for any Exercise you want.


# ________________________________________ 1 _________________________________________________ 
# Find closest number to 0. If there are multiple correct ansvers return biggest one.
# [0, 5, 2, -1, 1] => findClosestNumber => 0
# [2, 5, 8, 7, -1] => findClosestNumber => -1
# [-2, 2, 5, 4, 3, 7, 122, 52, 3, -1, 1] => findClosestNumber => 1

# Test cases:
nums1_0 = [5, 3, 2, 1, 4, 7, 2, -5, 7, -1, -4, -8] # => 1
nums1_1 = [2, 3, 1, 0, 8, 0, 2, 1, 4, 5, 6, 7, -1] # => 0
nums1_2 = [-1, -3, -2, -5, 1, 5, 2]                # => 1 

# Your solutions go here: vvvvvvvvvvvvvvvvvvvvvvvvvvvvvv


# print(findClosestNumber(nums = nums1_2))
# Your solution: ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
 
# Solution:
#print(arrAnswers.findClosestNumber(nums = nums1_2))



# ________________________________________ 2 _________________________________________________   
# Marge two strings ALTERNATLY togeather.
# Starting with word1.
# If word1 or word2 is longer than other, append rest of the string to end of returned string.

# Test CASES:
str1_0 = "abc"
str1_1 = "def"  # => "adbecf"

str2_0 = "ghijk"
str2_1 = "lmn"  # => "glhminjk"

# Your solutions go here: vvvvvvvvvvvvvvvvvvvvvvvvvvvvvv


# print(margeAlternately(str1 = str2_0, str2 = str2_1 ))
# Your solution: ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# Solution:
# print(arrAnswers.margeAlternately(str1 = str2_0, str2 = str2_1 ))                  



# ________________________________________ 3 _________________________________________________   
# Roman numbers as string converted to integer up to 4999
# I = 1
# V = 5
# X = 10
# L = 50
# C = 100
# D = 500
# M = 1000


# Test cases:
romanStr1 = "III"     # => 3
romanStr2 = "LVIII"   # => 58
romanStr3 = "MCMXCIV" # => 1994
romanStr4 = "IX"      # => 9

# Your solutions go here: vvvvvvvvvvvvvvvvvvvvvvvvvvvvvv





# print(romanToInt(romanNum = romanStr4))
# Your solution: ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# Solution:
#print(arrAnswers.romanToInt(romanNum = romanStr4))       


# ________________________________________ 4 _________________________________________________      
# Write function that returns boolean if first string is subsequence of second string
# Subsequence: characters are in same order in both subS* and string*. 
# subS1 = fbca => f: index 0, b: index 1, c: index 2
# string1 = "cdafb" => c: index 0, d: index 1, a: index 2, f: index 3, b: index 4
# character b in string1 have higher index than c. 
# character b in subS1 have lower index than c.
# That is why function should retun False.  

# Test cases:
subS1: str = "fbc"
string1: str = "cdafb"   # => False

subS2: str = "aaaa"
string2: str = "abbaaaa" # => True

# Your solutions go here: vvvvvvvvvvvvvvvvvvvvvvvvvvvvv




# print(isSubsequence(s = subS2, t = string2))
# Your solution: ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# Solution:
#print(arrAnswers.isSubsequence(s = subS2, t = string2))



# ________________________________________ 5 _________________________________________________ 
# Function that takes an list of integers and returns highest possible earning. 
# Indexes in list represents days.
# Lowest possible number need to have lower index than highest one due to index should represent a day on market
# YOU CAN'T sell earlier than you can buy STOCK from market.
# [1, 2, 4, 6, 7] => 6
# [7, 6, 5, 4, 2] => 0

# Test cases:
prices1: list[int] = [1, 2, 7, 8, 2, 6, 5, 4, 1, 7, 15, 2, 14, 3] # => 14
prices2: list[int] = [2, 1, 5, 7, 4, 1, 3, 7, 8]                  # => 7
prices3: list[int] = [7, 4, 2, 1]                                 # => 0

# Your solutions go here: vvvvvvvvvvvvvvvvvvvvvvvvvvvvv




#print(maxProfit(prices = prices3))
# Your solution: ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 

# Solution:
# print(arrAnswers.maxProfit(prices = prices3))



# ________________________________________ 6 _________________________________________________          
# Find longest common prefix in list of strings.
# Prefix: first matching characters in all strings within list.

# Test case:
strs0 = ["flower", "flow", "flight"]                            # => "fl"
strs1 = ["dog", "cat", "horse", "wood"]                         # => ""
strs2 = ["interspecies", "interstellar", "interstate", "inter"] # => "inter"
strs3 = ["a", "ab", "abc", "abcd"]                              # => "a"
strs4 = ["", "apple", "app"]                                    # => ""  
strs5 = [""]
strs6 = ["", "a"]
# Your solutions go here: vvvvvvvvvvvvvvvvvvvvvvvvvvvvv



#print(longestCommonPrefix(strs = strs1))
# Your solution: ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 

# Solution:
#print(arrAnswers.longestCommonPrefix(strs = strs2))



# ________________________________________ 7 _________________________________________________  

# Group the elements of array into ranges that are continuous.
# That is, in one range their should not be any number absent in array.
# And we need to minimize the different ranges we use, so try to take as big range as possible.
# At each element, make a different range only when you find some number absent in between current and last element,
# otherwise expand the current range by1

# Input: nums: list[int] = [0, 2, 3, 4, 6, 8, 9] => list[str] = ["0", "2->4", "6", "8->9"]

# Test case:
nums2_0: list[int] = [0, 2, 3, 4, 6, 8, 9 ]        # => ["0", "2->4", "6", "8->9"]
nums2_1: list[int] = [1, 3, 4, 5, 6, 8, 9, 12, 13] # => ["1", "3->6", "8->9", "12->13"]
nums2_2: list[int] = [0, 1, 2, 4, 5, 7]            # => ["0->2", "4->5", "7"] 
nums2_3: list[int] = [1, 3]                        # => ["1", "3"]
nums2_4: list[int] = []                            # => []  

# Your solutions go here: vvvvvvvvvvvvvvvvvvvvvvvvvvvvv




#print(summaryRanges( nums = nums2_0))
# Your solution: ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 

# Solution:
# print(arrAnswers.summaryRanges( nums = nums2_4))