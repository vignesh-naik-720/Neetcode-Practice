from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        values = self.store[key]
        left, right = 0, len(values) - 1
        result = ""

        while left <= right:
            mid = (left + right) // 2
            mid_time, mid_val = values[mid]

            if mid_time == timestamp:
                return mid_val
            
            elif mid_time < timestamp:
                result = mid_val
                left = mid + 1
                
            else:
                right = mid - 1

        return result
