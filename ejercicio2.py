from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
    
    def containsDuplicate2(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    return True
        return False
    

if __name__ == "__main__":
    solution = Solution()
    print("Fuerza bruta")
    # Case 1
    nums1 = [1, 2, 3, 1]
    print(f"Case 1: {nums1} → {solution.containsDuplicate2(nums1)}")
    
    # Case 2
    nums2 = [1, 2, 3, 4]
    print(f"Case 2: {nums2} → {solution.containsDuplicate2(nums2)}")
    
    # Case 3
    nums3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    print(f"Case 3: {nums3} → {solution.containsDuplicate2(nums3)}")

    print("optimo")
    # Case 1
    nums1 = [1, 2, 3, 1]
    print(f"Case 1: {nums1} → {solution.containsDuplicate(nums1)}")
    
    # Case 2
    nums2 = [1, 2, 3, 4]
    print(f"Case 2: {nums2} → {solution.containsDuplicate(nums2)}")
    
    # Case 3
    nums3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    print(f"Case 3: {nums3} → {solution.containsDuplicate(nums3)}")
