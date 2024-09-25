from answers import hashMapsAns as ans

# ________________________________________ 1 _________________________________________________ 
# You're given strings jewels representing the types of stones that are jewels.
# Stones representing the stones you have.
# Each character is stones is a type of stone you have.
# How many of the stones you have are also jewels. 

# jewels = "abc"   stones="aabccddee" => 5 jewels in stones.
# "a" is different type of jewel than "A". 

# Test case:
jewels: str = "aA"
stones: str = "aAAbbb"  # => 3

jewels1: str = "z"
stones1: str = "ZZ"  # => 0

# Your solutions go here: vvvvvvvvvvvvvvvvvvvvvvvvvvvvvv


#print(numJewelsInStones(jewels = jewels, stones = stones))
# Your solution: ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 

# Solution:
# print(ans.numJewelsInStones(jewels = jewels1, stones = stones1))



# ________________________________________ 2 _________________________________________________ 
# Return true or false if list contains duplicates.
nums_1: list[int] = [1, 2, 3, 4, 5]  # => False
nums_2: list[int] = [1, 1, 2, 3, 4, 5] # => True

# Your solutions go here: vvvvvvvvvvvvvvvvvvvvvvvvvvvvvv


# print(containsDuplicates(nums = nums_1))
# Your solution: ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 

# Solution:
# print(ans.containsDuplicates(nums = nums_2))



# ________________________________________ 3 _________________________________________________ 
# Given two strings ransomNote and magazine,
# return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Test cases
ransomNote1, magazine1 = "a", "b"                  # => False
ransomNote2, magazine2=  "lopata", "kloktalaporum" # => True
ransomNote3, magazine3 = "abc", "abbaccdfgrtl"     # => True
ransomNote4, magazine4 = "aa", "aab"               # => True

# Your solutions go here: vvvvvvvvvvvvvvvvvvvvvvvvvvvvvv





# print(canConstruct(ransomNote = ransomNote1, magazine = magazine1 ))
# Your solution: ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 

# Solution:
#print(ans.canConstruct(ransomNote = ransomNote4, magazine = magazine4))



# ________________________________________ 4 _________________________________________________ 
# Create function that returns boolean value if strings s and t are anagrams.

s1, t1 = "jelenovipivonelej", "jelenovipivonelej"  # True 
s2, t2 = "a", "ab"                                 # False
s3, t3 = "abc", "cab"                              # True  
# Your solutions go here: vvvvvvvvvvvvvvvvvvvvvvvvvvvvvv



# print(isAnagram(s = s1, t = t1))
# Your solution: ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 

# Solution
# print(ans.isAnagram(s=s1, t=t1))

# ________________________________________ 5 _________________________________________________ 
# Return maximum numbers of Balloons in string

st1: str = "ballvnvbllvooccossonaaaoarrvv" # => 2
st2: str = "nlaebolko"                     # => 1
st3: str = "leetcode"                      # => 0
st4: str = "loonbalxballpoon"              # => 2
st5: str = "krhizmmgmcrecekgyljqkldocicziihtgpqwbticmvuyznragqoyrukzopfmjhjjxemsxmrsxuqmnkrzhgvtgdgtykhcglurvppvcwhrhrjoislonvvglhdciilduvuiebmffaagxerjeewmtcwmhmtwlxtvlbocczlrppmpjbpnifqtlninyzjtmazxdbzwxthpvrfulvrspycqcghuopjirzoeuqhetnbrcdakilzmklxwudxxhwilasbjjhhfgghogqoofsufysmcqeilaivtmfziumjloewbkjvaahsaaggteppqyuoylgpbdwqubaalfwcqrjeycjbbpifjbpigjdnnswocusuprydgrtxuaojeriigwumlovafxnpibjopjfqzrwemoinmptxddgcszmfprdrichjeqcvikynzigleaajcysusqasqadjemgnyvmzmbcfrttrzonwafrnedglhpudovigwvpimttiketopkvqw"
# Your solutions go here: vvvvvvvvvvvvvvvvvvvvvvvvvvvvvv



# print(maxNumberOfBalloons(text: str))
# # Your solution: ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 

# Solution:
print(ans.maxNumberOfBalloons(text = st5))
