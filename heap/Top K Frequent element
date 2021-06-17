from heapq import heappush, heappop

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return [nums[0]]
        #keep track the counter
        hashmap = {} 
        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1
        heap =[]
        for key in hashmap:
            heapq.heappush(heap, ((hashmap[key], key))) #(freq, unique number)
            if len(heap) > k:
                heapq.heappop(heap)
        ans =[]
        while heap:
            freq, element = heapq.heappop(heap)
            ans.append(element)
        return ans
or 
        ans = []
        for element in heap:
            ans.append(element[1]) #get the number
        return ans
Time = O(n log(k))
Space = O(n)

