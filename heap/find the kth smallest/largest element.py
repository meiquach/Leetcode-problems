#Time: O(nlogn)
class Solution:
  def kthSmallest(self, nums, k):
    heap = []
    for i in range(nums):
      heapq.heappush(heap, nums[i])
    ans = None
    
    for j in range(k):
      ans = heapq.heappop(heap)
    return ans
  
# Time: O(nlogk)
class Solution:
  def kthSmallest(self, nums, k):
    heap = []
    for i in range(len(nums)):
      heapq.heappush(heap, -nums[i]) #negate it, change to maxheap 
      if len(heap) > k:
        heapq.heappop()
    return -heapq.heappop() #return the negate
""can use QuickSelect""

# Time: O(nlogn)
class Solution:
  def kthLargest(self, nums: List[int], k):
    heap = []
    for i in range nums:
      heapq.heappush(heap, -nums[i])
or  for i in nums:
      heapq.heappush(heap, -i)
    
    for j in range(k):
      ans = -heapq.heappop(nums)
    return ans
  
# Time: O(nlogk)
class Solution:
    def KthLargest(self, nums: List[int], k: int) -> int:
      heap = []
      for i in nums:
        heapq.heappush(heap,i) #minheap
        if len(heap) > k:       
           heapq.heappop(heap)
      return heapq.heappop(heap)
      
      
     
      
