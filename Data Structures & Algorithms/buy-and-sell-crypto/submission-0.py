class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_window = len(prices)-1
        curr_window = 1
        max_profit = 0
        buy = 0
        i,j = 0,1
        while curr_window <= max_window:
            print(i,j,curr_window)
            max_profit = max(max_profit, (prices[j]-prices[i]))
            i+=1
            j+=1
            if j==len(prices):
                curr_window += 1
                i = 0
                j = curr_window
        
        return max_profit