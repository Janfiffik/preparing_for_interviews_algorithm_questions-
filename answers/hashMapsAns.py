# Imports
from collections import Counter
import math

# _______________________________________ 1 ____________________________________________
def numJewelsInStones(jewels: str, stones: str) -> int:
    jewelsSet: set = set(jewels)  # => make set from jewels string. Gets rid of duplicates and it is faster iterate over set. 
             
    return sum(1 for stone in stones if stone in jewelsSet) # add 1 to sum() if stone from stones string is inside jewelsSet.
                                                            # Than return sum() of all 1.
                                                            
# _______________________________________ 2 ____________________________________________      
def containsDuplicates(nums: list[int]) -> bool:
    return len(set(nums)) != len(nums) 


# _______________________________________ 3 ____________________________________________
def canConstruct(ransomNote: str, magazine: str) -> bool:
    
    ranDict: dict = Counter(ransomNote)         # => Creates dictionary character as key count as value
    magDict: dict = Counter(magazine)           # => Creates dictionary character as key count as value
    
    for char in ranDict.keys():
        if char not in magDict.keys() or ranDict[char] > magDict[char]:  
        # Check if character is not in magazine dictionary or its value inside magDict is higher than in ranDict: => True  returns False
            return False
        else:                 # Else continue
            continue        
    return True               
                        

# _______________________________________ 4 ____________________________________________    
def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):   # Checks if both stings are same length. If not they are certanli not anagrams 
        return False
    
    sDict = Counter(s)  # Creates dict from s string characters are keys character counts are values.
    tDict = Counter(t)  # Same thing
    
    for i in sDict.keys():  # For character in sDict keys:
        if i not in tDict.keys() or tDict[i] != sDict[i]:  # If character is not in other dict or  values are not same 
            return False                                   # Is not anagram
        
    return True                                            # Else is anagram 

# _______________________________________ 5 ____________________________________________  
def maxNumberOfBalloons(text: str) -> int:
    textDict = Counter(text)
    required_chars = "balon"
    required_counts = {'b': 1, 'a': 1, 'l': 2, 'o': 2, 'n': 1}
    
    counter: int= 999999
    
    for char in required_chars:
        
        if char not in textDict:
            return 0
        
        char_count = textDict[char] // required_counts[char]
        
        counter = min(counter, char_count)
        
    return counter
    
        
            
           
                    