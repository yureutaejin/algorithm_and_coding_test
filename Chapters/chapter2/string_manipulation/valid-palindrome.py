# check setence is palindrome or not
from time import time
import collections

def palindrome_list(s: str) -> bool:
    strs: list = list(map(lambda x: x.lower(), filter(lambda x: x.isalnum(), s)))
    
    while len(strs) > 1:
        if strs.pop(0)!=strs.pop():
            return False 
    return True

def palindrome_deque(s: str) -> bool:
    strs: Deque = collections.deque()
    [strs.append(i.lower()) for i in s if i.isalnum()]
    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False
    return True
    

def palindrome_slicing(s: str) -> bool:
    s: list = [i.lower() for i in s if i.isalnum()]
    return s == s[::-1]
    
    

if __name__ == "__main__":
    # test cases
    examples = ["A man, a plan, a canal: Panama", "race a car"]
    
    # answer
    # True, False
    start = time()
    [print(palindrome_slicing(example)) for example in examples]
    print(f"runtime: {time() - start}")