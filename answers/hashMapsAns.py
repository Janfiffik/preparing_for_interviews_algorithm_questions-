# _______________________________________ 1 ____________________________________________
def numJewelsInStones(jewels: str, stones: str) -> int:
    jewelsSet: set = set(jewels)  # => make set from jewels string. Gets rid of duplicates and it is faster iterate over set. 
             
    return sum(1 for stone in stones if stone in jewelsSet) # add 1 to sum() if stone from stones string is inside jewelsSet.
                                                            # Than return sum() of all 1. 