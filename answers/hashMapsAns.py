# _______________________________________ 1 ____________________________________________
def numJewelsInStones(jewels: str, stones: str) -> int:
    jewelsSet: set = set(jewels)  # => make set from jewels string. Gets rid of duplicates and it is faster iterate over set. 
             
    return sum(1 for stone in stones if stone in jewelsSet) # add 1 to sum() if stone from stones string is inside jewelsSet.
                                                            # Than return sum() of all 1.
                                                            
# _______________________________________ 2 ____________________________________________      
def containsDuplicates(nums: list[int]) -> bool:
    return len(set(nums)) != len(nums) 


# _______________________________________ 3 ____________________________________________
from collections import Counter

def canConstruct(ransomNote: str, magazine: str) -> bool:
    ranDict: dict = Counter(ransomNote)         # => Creates dictionary character as key count as value
    magDict: dict = Counter(magazine)           # => Creates dictionary character as key count as value
    
    for char in ranDict.keys():
        if char not in magDict.keys() or ranDict[char] > magDict[char]:  
        # Check if character is not in magazine dictionary or its value inside magDict is higher than in ranDict:
            return False
        else:
            continue        
    return True   
                        
    