
# url: https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array/

def kthLargestNumber(nums: list[str], k: int) -> str:
        
        ints = [int(x) for x in nums]
        ints.sort(reverse=True)

        return str(ints[k-1])
    
    
nums = input().split()
k = int(input())

print(kthLargestNumber(nums, k))