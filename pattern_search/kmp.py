def fill_lps(s,):
    
    n = len(s)
    l = 0
    lps = [0 for i in range(n)]
    i = 1
    while i < n:
        if s[i] == s[l]:
            l += 1
            lps[i] = l
            i += 1
        else:
            if l == 0:
                lps[i] = 0
                i += 1
            else:
                l = lps[l -1]
    return lps



def kmp(text,pat):
    n = len(text)
    m = len(pat)
    
    lps = fill_lps(pat)
    i,j = 0,0
    
    while i < n:
        if pat[j] == text[i]:
            i += 1
            j += 1
        if j == m:
            print(i-j)
            j = lps[j-1]
        elif i < n and pat[j] != text[i]:
            if j == 0:
                i += 1
            else:
                j = lps[j-1]
                
kmp("abcabcdabc","abc")