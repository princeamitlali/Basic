#  suppose only one repetative element

li = [0,1,3,2,4,6,5,7,3]

def find_repeating_starting_with_1(li):
    n = len(li)
    
    slow,fast = li[0],li[0]
    
    while True:
        slow = li[slow]
        fast = li[li[fast]]
        if slow == fast:
            break
    
    slow = li [0]
    while slow != fast:
        slow = li[slow]
        fast = li[fast]
        
    return slow

print(find_repeating_starting_with_1(li[1:]))


def find_repeating_starting_with_0(li):
    n = len(li)
    
    slow,fast = li[0]+1,li[0]+1
    
    while True:
        slow = li[slow] + 1
        fast = li[li[fast]+1]+1
        if slow == fast:
            break
    
    slow = li [0] +1
    while slow != fast:
        slow = li[slow]+1
        fast = li[fast]+1
        
    return slow-1

print(find_repeating_starting_with_0(li))