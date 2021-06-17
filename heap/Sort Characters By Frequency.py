class Solution:
    def frequencySort(self, s: str) -> str:
        hashmap = {}
        for num in s:
            if num in hashmap:
                hashmap[num] +=1
            else:
                hashmap[num] = 1
        #sort character according to its frequency(largest to smallest)
        s = sorted(hashmap, key = lambda k:hashmap[k], reverse = True)
        result = ""
        for i in s:
            result += i * hashmap[i] #add the char with its own times
        return result
Time: O(nlogn)
-----------------------------------------------------------------------------
class Solution:
    def frequencySort(self, s: str) -> str:
        hashmap = {}
        for num in s:
            if num in hashmap:
                hashmap[num] +=1
            else:
                hashmap[num] = 1
        heap = []
        for key in hashmap:
            heapq.heappush(heap, (-hashmap[key],key))
        result = ""
        while heap:
            freq, char = heapq.heappop(heap)
            result += -freq * char
        return result
Time: O(nlogn)
