class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        if not self.minHeap or num < self.minHeap[0]:
            heapq.heappush(self.maxHeap, -1 * num)
        else:
            heapq.heappush(self.minHeap, num)
        if len(self.maxHeap) - len(self.minHeap) > 1:
            heapq.heappush(self.minHeap, -1 * heapq.heappop(self.maxHeap))
        if len(self.minHeap) - len(self.maxHeap) > 1:
            heapq.heappush(self.maxHeap, -1 * heapq.heappop(self.minHeap))
        

    def findMedian(self) -> float:
        if len(self.maxHeap) == len(self.minHeap):
            return ((-1 * self.maxHeap[0]) + self.minHeap[0]) / 2
        elif len(self.maxHeap) > len(self.minHeap):
            return -1 * self.maxHeap[0]
        else:
            return self.minHeap[0]

        
        