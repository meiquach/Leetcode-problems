class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if k == 0 or len(nums1) == 0 or len(nums2) ==0: #base case
            return []
        
        heap =[]
        #we don't have to go thro all of the element in the array instead just neeed to go
        #to k element because the given array is already sorted(ascending)
        for i in range(0, min(k, len(nums1))):
            for j in range(0, min(k,len(nums2))):
                x,y = nums1[i], nums2[j]
                sum = x + y
                heapq.heappush(heap, [-sum, x,y])
                if len(heap)>k: #when heap exceeds the k, pop out
                    heapq.heappop(heap)
        ans = []
        while heap:
            sum, x, y = heapq.heappop(heap)
            ans.append((x,y))
        return ans
 Time: O(nlogn)
 
 
