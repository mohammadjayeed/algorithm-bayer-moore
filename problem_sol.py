def majorityElement(nums):
        count = 0
        cursor = nums[0]
        for i in range(0,len(nums)):
                if cursor == nums[i]:
                        count+=1
                else:
                        count -=1

                if count == -1:
                        cursor = nums[i]
                        count = 1
                        
        return cursor