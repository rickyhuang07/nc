class TimeMap:

    def __init__(self):
        self.x = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.x[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        lst = self.x[key]
        left, right = 0, len(lst) - 1
        while left <= right:
            mid = (left + right) // 2
            if lst[mid][0] <= timestamp:
                res = lst[mid][1]
                left = mid + 1
            else:
                right = mid - 1
        return res

        
        
