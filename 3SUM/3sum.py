    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums = sorted(nums)
        n = len(nums)
        triplet_set = set() 
        for ind in range(n):
            zero1 = -nums[ind]
            i,j = ind+1, n-1
            while i<j:
                zero2 = nums[i] + nums[j]
                if zero2<zero1:
                    i+=1
                elif zero2>zero1:
                    j-=1
                else:
                    triplet_set.add((nums[ind],nums[i],nums[j]))
                    i+=1
                    j-=1
        return triplet_set
