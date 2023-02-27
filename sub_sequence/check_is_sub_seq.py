'''
check string 1 is an subsequence of string 2 or not
'''

def subseq_checker(s1:str,s2:str) -> bool:
    i,j = 0,0
    while i < len(s1) and j < len(s2):
        if s1[i] == s2[j]:
            j += 1
        i += 1
    return j == len(s2)

print(subseq_checker("g","e"))