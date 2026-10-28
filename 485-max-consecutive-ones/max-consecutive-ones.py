class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        oneCount=0
        maxCount=0
        for i in range(len(nums)):
            if nums[i]!=1:
                if oneCount > maxCount:
                    maxCount=oneCount
                oneCount=0
            else:
                oneCount+=1
        return max(maxCount,oneCount)