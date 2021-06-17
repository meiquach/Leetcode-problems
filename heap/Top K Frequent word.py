class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        hashmap ={} #using hashmap to count the frequent
        for word in words:
            if word in hashmap:
                hashmap[word] += 1
            else:
                hashmap[word] =1
        heap = []
        for key in hashmap:
            heapq.heappush(heap, (-hashmap[key], key)) #times, unique word
        res = []
        for i in range (k):
            pop = heapq.heappop(heap)
            res.append(pop)
        #sort by alphabetical
        res.sort()
        ans = []
        for word in res:
            ans.append(word[1]) #because word 0 is times
        return ans
Time: O(nlogn)
