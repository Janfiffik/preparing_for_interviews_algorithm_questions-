from answers import arrayAnswers as answers

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
 
# Answer:
#print(answers.findClosestNumber(nums = nums1_2))



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

# Answer:
# print(answers.margeAlternately(str1 = str2_0, str2 = str2_1 ))                  



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

# Answer:
#print(answers.romanToInt(romanNum = romanStr4))       


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

# Answer:
#print(answers.isSubsequence(s = subS2, t = string2))



# ________________________________________ 5 _________________________________________________ 
# Function that takes an list of integers and returns highest possible. 
# Indexes in list represents days.
# Lowest possible number need to have lower index than highest one due to index should represent a day on market
# YOU CAN'T sell earlier than you buy STOCK from market
# [1, 2, 4, 6, 7] => 6
# [7, 6, 5, 4, 2] => 0




# Test cases:
prices1: list[int] = [1, 2, 7, 8, 2, 6, 5, 4, 1, 7, 15, 2, 14, 3] # => 14
prices2: list[int] = [2, 1, 5, 7, 4, 1, 3, 7, 8]                  # => 7
prices3: list[int] = [7, 4, 2, 1]                                 # => 0
 
# print(maxProfit(prices = prices3))
         