class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = []
        lead = -float('inf')
        count = 0
        for i in range (len(position)):
            arr.append((position[i], speed[i]))
        arr.sort(key = lambda x: -x[0])
        for tup in arr:
            time = (target - tup[0]) / tup[1]
            if time > lead:
                lead = time
                count += 1
        return count
        


                    

