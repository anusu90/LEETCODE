class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        sol = []
        n=len(nums)
        used = [False]*n
        curr=[]
        def dfs(used,temp):
            if(len(temp)==n):
                sol.append(temp[::])
                return
            for i in range(n):
                if used[i]==True:
                    continue
                used[i]=True
                temp.append(nums[i])
                dfs(used,temp)
                used[i]=False
                temp.pop()
            
        dfs(used,curr)
        return sol
        