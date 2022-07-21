li = [1,5,3,8,12]

def max_profit(price,start,end):
    if end <= start:
        return 0
    profit = 0
    for i in range(start,len(price)):
        for j in range(i+1,len(price)):
            if price[j] > price[i]:
                curr_profit = price[j] - price[i] + max_profit(price,start,i-1) + max_profit(price,j+1,end)
                
                profit = max(profit,curr_profit)
        return profit
    
val = max_profit(li,0,len(li))
print(val)