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
print(ans.numJewelsInStones(jewels = jewels1, stones = stones1))