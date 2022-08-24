def findSubstring(s: str, words):
        length = sum(len(i) for i in words) 
        op = []
        for i in range(len(s)-length+1):
            temp = s[i:i+length]
            for j in words:
                if j in temp:
                    print(temp,j)

                    ind = temp.index(j)
                    le = ind +  len(j)
                    
                    temp = temp[:le].replace(j,"") + temp[le:]
            # print(temp)    
            if len(temp) == 0:
                op.append(i)
                
        return op
        
        
print(findSubstring("goodgoodbestword",["word","good","best","good"]))