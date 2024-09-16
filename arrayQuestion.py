# These questions comes from [https://algomap.io/]

# 1------------------------------------------------------------------------------------. 
# Find closest number to 0. If there are multiple correct ansvers return biggest one.
# [0, 5, 2, -1, 1] => findClosestNumber => 0
# [2, 5, 8, 7, -1] => findClosestNumber => -1
# [-2, 2, 5, 4, 3, 7, 122, 52, 3, -1, 1] => findClosestNumber => 1


def findClosestNumber(nums: list[int]) -> int:
    """_summary_

    Args:
        nums (list[int]): function accepts array of numbers
        and return number closest to 0.
        If there are multiple answers returns biggest one.
    Returns:
        int: 
        closest number to 0.
    """
    closest = nums[ 0 ]
    for i in nums:
        if abs(i) < abs(closest) or (abs(i) == abs(closest) and i > closest):
            closest = i            
        
    return closest

# Test cases:

nums1_0 = [5, 3, 2, 1, 4, 7, 2, -5, 7, -1, -4, -8] # => 1
nums1_1 = [2, 3, 1, 0, 8, 0, 2, 1, 4, 5, 6, 7, -1] # => 0
nums1_2 = [-1, -3, -2, -5, 1, 5, 2]                # => 1 

# print(findClosestNumber(nums=nums1_2))

# 2------------------------------------------------------------------------------------.    
# Marge two strings ALTERNATLY togeather.
# Starting with word1.
# If word1 or word2 is longer than other, append rest of the string to end of returned string.


def margeAlternately(str1: str, str2: str) -> str:
    wordlen1 = len(str1)
    wordlen2 = len(str2)
    wordLen = 0
    newString = ""  
    if wordlen1 < wordlen2:
        wordLen = wordlen1
    else:
        wordLen = wordlen2
    
    for i in range(0, wordLen):
        newString += str1[i]
        newString += str2[i]
    
    if wordlen1 > wordlen2:
        newString += str1[wordlen2:]
    elif wordlen1 < wordlen2:
        newString += str2[wordlen2:]  
    
    return newString

# Test cases:
str1_0 = "abc"
str1_1 = "def"  # => "adbecf"

str2_0 = "ghijk"
str2_1 = "lmn"  # => "glhminjk"

# print(margeAlternately(str1 = str2_0, str2 = str2_1 ))                  

# 3------------------------------------------------------------------------------------.  
# Roman numbers converted to integer
# I = 1
# V = 5
# X = 10
# L = 50
# C = 100
# D = 500
# M = 1000


def romanToInt(romanNum: str) -> int:
    romanNumbers: dict = {
        "I": 1, "V": 5, "X": 10,
        "L": 50, "C": 100, "D": 500,
        "M": 1000
    }
    strToArr: list[str] = [i for i in romanNum] # -> convert str to and array
    arrToNums: list[int] = []
    
    for i in range(len(strToArr)):
        number: int = romanNumbers[strToArr[i]]
        arrToNums.append(number)
        
        if i > 0 and number > arrToNums[i - 1]:
            arrToNums[i] = arrToNums[i] - 2 * arrToNums[i-1]
            
    return sum(arrToNums)

# Test cases:
romanStr1 = "III"     # => 3
romanStr2 = "LVIII"   # => 58
romanStr3 = "MCMXCIV" # => 1994
romanStr4 = "IX"        # => 9

#print(romanToInt(romanNum = romanStr4))       

# 4------------------------------------------------------------------------------------.     
# Write function that returns boolean if first string is subsequence of second string
def isSubsequence(s: str, t: str) -> bool:
    i: int = 0
    for char in t:
        if i < len(s) and s[i] == char:
            i += 1
    return i == len(s)

# Test cases:

subS1: str = "fbc"
string1: str = "cdafb"   # => False

subS2: str = "aaaa"
string2: str = "abbaaaa" # => True

#print(isSubsequence(s = subS2, t = string2))

# 5------------------------------------------------------------------------------------.
# Function that takes an list of integers and returns highest possible. 
# Lowest possible number need to have lower index than highest one due to index should represent a day on market
# [1, 2, 4, 6, 7] => 6
# [7, 6, 5, 4, 2] => 0


def maxProfit(prices: list[int]) -> int:
    highest: int = 0
    min_price: int = prices[0]
    
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > highest:
            highest = price - min_price
    
    return highest 

# Test cases:
prices1: list[int] = [1, 2, 7, 8, 2, 6, 5, 4, 1, 7, 15, 2, 14, 3] # => 14
prices2: list[int] = [2, 1, 5, 7, 4, 1, 3, 7, 8]                  # => 7
prices3: list[int] = [7, 4, 2, 1]                                 # => 0
 
# print(maxProfit(prices = prices3))
         