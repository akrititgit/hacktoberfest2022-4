def jump(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[0]*n
        for i in range(n-2,-1,-1):
            min1=float('inf')
            for j in range(i+1,min(n,i+nums[i]+1)):
                min1=min(min1,dp[j])
            dp[i]=1+min1
        return dp[0]
