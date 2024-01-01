class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort(reverse= True)
        processorTime.sort()
        time = []
        for i in range(len(processorTime)):
            time.append(processorTime[i] + tasks[i*4])                     
        return max(time)

            
        