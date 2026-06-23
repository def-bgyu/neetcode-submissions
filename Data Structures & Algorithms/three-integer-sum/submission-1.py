class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []

        nums_sorted = sorted(nums)

        for i in range(len(nums_sorted)):
            if i > 0 and nums_sorted[i] == nums_sorted[i-1]:
                continue
            ptr1 = i +1
            ptr2 = len(nums_sorted) -1
            while ptr1< ptr2:
                sum = nums_sorted[ptr1] + nums_sorted[ptr2]
                if sum == -(nums_sorted[i]):
                    result.append([nums_sorted[i], nums_sorted[ptr1], nums_sorted[ptr2]])
                    ptr1 +=1
                    ptr2 -=1
                    while ptr1 < ptr2 and nums_sorted[ptr1] == nums_sorted[ptr1-1]:
                        ptr1 += 1
                    while ptr1 < ptr2 and nums_sorted[ptr2] == nums_sorted[ptr2+1]:
                        ptr2 -= 1
                elif sum > -nums_sorted[i]:
                    ptr2 -= 1
                elif sum < -nums_sorted[i]:
                    ptr1 += 1    
        return result