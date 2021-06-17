class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key= lambda k: k[0]**2 + k[1]**2) #formula for Euclidean distance
        return points[:k]
      
Heap solution:
#observation
1. create a max heap to store (point's distance to original, point)
1.1: write the formula to find the distance
2. if heap size exceeds the k, then we pop from the heap
3.return the heappop
Time: O(nlogk)
Space: O(k)
                               
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            dist = point[0]**2 + point[1]**2 		#point's distance from origin
            heapq.heappush(heap,(-dist, point)) #maxheap
            if len(heap) > k:
                heapq.heappop(heap)
#return the point pair of all the elements in the heap, tuple[0] is the -distance so we do not need it for the answer here 
        return [word[1] for word in heap]
or
        ans =[]
        for word in heap:
            ans.append(word[1])
        return ans]
or
        ans = []
        while heap:
            dist, point = heapq.heappop(heap)
            ans.append(point)
        return ans
