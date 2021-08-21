    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        nums = sorted(nums)
        diff = float("infinity")
        n = len(nums)
        for ind in range(n):
            i,j= ind+1,n-1
            while i<j:
                target2= nums[i] + nums[j] + nums[ind]
                diff2 = abs(target - target2)
                if  diff2<diff:
                    diff=diff2
                    ans=target2
                if target2>target:
                    j-=1
                else:
                    i+=1
        return ans
