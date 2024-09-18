
# -----------------SOLUTION 1---------------------------------
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
    closest: int = nums[ 0 ]
    for i in nums:  # Iterates over list of integers
        if abs(i) < abs(closest) or (abs(i) == abs(closest) and i > closest): 
            # Checks if absolute value of i 'ABSOLUTE VALUE IS: (-5) ->5' is lower than absolute value of closest variable.
            # Or absolute value of i is strictli equal to absolute value of closest.
            # AND i is bigger than closest 
            # IF thouse conditions are true asign i as value for CLOSEST variable    
            closest = i            
        
    return closest  # Return closest number to 0 or 0.



# -------------------------------SOLUTION 2-------------------------------
def margeAlternately(str1: str, str2: str) -> str:
    wordlen1: int = len(str1)
    wordlen2: int = len(str2)
    wordLen: int = 0
    newString: str = ""
    
    # Checks which word is shorter for next for loop to avoid Index out of range.   
    if wordlen1 < wordlen2:
        wordLen = wordlen1
    else:
        wordLen = wordlen2
    
    # Loops ower both words and add characters one by one to newString 
    for i in range(0, wordLen):
        newString += str1[i]
        newString += str2[i]
    
    # Appends rest of longest word to newString variable by using list slicing
    if wordlen1 > wordlen2:
        newString += str1[wordlen2:]
    elif wordlen1 < wordlen2:
        newString += str2[wordlen2:]  
    
    return newString # Returns newString



# -------------------------------SOLUTION 3-------------------------------
def romanToInt(romanNum: str) -> int:
    romanNumbers: dict = {
        "I": 1, "V": 5, "X": 10,
        "L": 50, "C": 100, "D": 500,
        "M": 1000
    } # Created dictionary for character values they are representing. 
    
    strToArr: list[str] = [i for i in romanNum] # -> convert str to list of characters
    arrToNums: list[int] = []                   # -> values from thouse characters.  
    
    for i in range(len(strToArr)):
        number: int = romanNumbers[strToArr[i]] # Gets value of character from dictionary
        arrToNums.append(number)                # Appends value to arrToNums list.
        
        # Checks if lower value is earlier in list than bigger one to get numbers like IX => 9
        if i > 0 and number > arrToNums[i - 1]:
            # if is True:            
            # [1, 10] => if is true
            # arrToNums[i] = arrToNums[i] - 2 * arrToNums[i-1] 
            # Once to undo the addition of the smaller numeral.
            # Once more to apply the correct subtraction rule for roman numbers.
            # [1, (10)] =[1, (10 - 2 * 1)] = [1, (10 - 2)] = [1, 8] => 9
            arrToNums[i] = arrToNums[i] - 2 * arrToNums[i-1]
            
    return sum(arrToNums) # sum function returns absolute value of list [ 1 + 8 ] => 9


# -------------------------------SOLUTION 4-------------------------------
def isSubsequence(s: str, t: str) -> bool:
    i: int = 0
    for char in t:
        if i < len(s) and s[i] == char:
            i += 1
    return i == len(s)


# -------------------------------SOLUTION 5-------------------------------
def maxProfit(prices: list[int]) -> int:
    highest: int = 0
    min_price: int = prices[0]
    
    for price in prices:                    # Iterates trough list prices.
        if price < min_price:               # Checks if current price is lower than min_price
            min_price = price               # If True. price assign as new min_price 
        elif price - min_price > highest:   # checks if price - min_price > highest
            highest = price - min_price     # if True new highest is created 
                                            # If all iteration fails highest stay 0
    return highest 


# -------------------------------SOLUTION 6-------------------------------
def longestCommonPrefix(strs: list[str]) -> str:
    if not strs:
            return ""                                                 # If there are no values in list just return ""
 
    shortestWord: str = min(strs, key=len)                            # Gets shortest word from list

    wordIndex: int = 0    
    while len(strs) > wordIndex:
        isItPrefix: bool = strs[wordIndex].startswith(shortestWord)   # Gets bool TRUE OR FALSE for shortestWord in strs
        if isItPrefix:                                                # If True Jumps on other word 
            wordIndex += 1
        elif not isItPrefix:                                          # if False shortestWord get rid of last character
            shortestWord = shortestWord[:-1]                          # If length of shortestWord becomes 0 returns ""
            if len(shortestWord) == 0:                                # Else continue in loop 
                return ""
        return shortestWord                                           # After executing whole for loop returns shortestWord 
    
    
    
# -------------------------------SOLUTION 7-------------------------------    
def summaryRanges(nums: list[int]) -> list[str]:                       
    new_range: str = ""                                               # variable for storing range string
    rangeNum: int = 0                                                 # variable used for comparison of current itteration and last rangeNum
    rangeList: list[str] = []                                         # list of ranges for returning
    
    for i in range(len(nums)):                                        # Iterates trough list of given numbers
        nextNum: int = nums[i+1] if i + 1 < len(nums) else nums[i]    # ternary operation for getting next Number      
        
        if not new_range:                                             # Checks if new_range is empty string 
            new_range += f"{nums[i]}"                                 # Appending current number to new_range string
            rangeNum = nums[i]                                        # rangeNum = current number from list
            
            if i == len(nums) - 1:                                    # if it is last itteration
                rangeList.append(new_range)                           # appends new_range string to list   
                return rangeList                                      # Returns rangeList as output of function 
            
        elif rangeNum + 1 == nums[i] and nums[i] == nextNum - 1:      # compares if last iteration +1 and current one and next iteration are continuous numbers  
            rangeNum = nums[i]                                        # If True current num becomes rangeNum in next itteration
            continue                                                  # Skips to next itteration
        
        elif rangeNum + 1 == nums[i] and nums[i] != nextNum - 1:      # Checks if last and current numbers are continous.   
            new_range += f"->{nums[i]}"                               # If True current number is apended to new_range string as ->currentNum" 
            rangeList.append(new_range)                               # Appends finished new_range to rangeList
            new_range = ""                                            # resets new_range and rangeNum to empty string and 0
            rangeNum = 0
               
        else:
            rangeList.append(new_range)                               # If all upper conditions fails therefore number is not continous from any side 
            new_range = f"{nums[i]}"                                  # appends number to newRange
            rangeNum = nums[i] 
                  
            if i == len(nums) - 1:                                    # If number was last 
                rangeList.append(f"{nums[i]}")                        # Append it and return whole rangeList
                return rangeList
                 
            
    return rangeList        