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