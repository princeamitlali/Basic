def index_of_left_repeating(s):
    for i in range(len(s)):
        if s[i] in s[i+1:]:
            return i
    return -1

print(index_of_left_repeating("fs"))