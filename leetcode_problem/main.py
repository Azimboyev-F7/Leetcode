class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        mid = 0
        high = len(nums) - 1

        # basic binary search algorithm
        while low <= high:
            mid = low + (high - low) // 2

            print(low, mid, high)

            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                low = mid + 1

            else:
                high = mid - 1

        ''' final position where to insert the target variable if not 
         present in the array '''
        if nums[mid] < target:
            return mid + 1
        return mid