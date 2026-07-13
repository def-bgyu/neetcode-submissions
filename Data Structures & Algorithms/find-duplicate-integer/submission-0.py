class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        #Given the conditions of the array, we will use fast and slow ptrs and traverse array like a LL

        # Similar yo find start point of a cycle

        slow = fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break # send slow to start 
        
        slow2 = 0
        while slow2 != slow:
            slow = nums[slow]
            slow2 = nums[slow2]

        return slow