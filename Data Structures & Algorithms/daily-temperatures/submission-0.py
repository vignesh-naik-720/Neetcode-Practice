class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] 
        result = [0] * len(temperatures)
        
        for curr_day, curr_temp in enumerate(temperatures):
            while stack and curr_temp > temperatures[stack[-1]]:
                prev_day = stack.pop()
                result[prev_day] = curr_day - prev_day
            stack.append(curr_day)
            
        return result

# temperatures = [30,38,30,36,35,40,28]
# stack = [], result = [0,0,0,0,0,0,0]
# curr_day = 0, curr_temp = 30
# while stack ? <-- false
# stack = [0]
# curr_day = 1, curr_temp = 38
# while stack <-- true and curr_temp > temperatures[stack[-1]] <-- 38 > 30 <-- true
# prev_day = 0, stack = []
# result[0] = 1 - 0 = 1 <-- result = [1,0,0,0,0,0,0] 
