class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        heap=[-1*x for x in stones]
        heapq.heapify(heap)

        while len(heap)>1:
            firstdata=heapq.heappop(heap)
            seconddata=heapq.heappop(heap)
            if firstdata!=seconddata:
                heapq.heappush(heap,firstdata-seconddata)
        if len(heap)==0:
            return 0
        return -1*heap[0]