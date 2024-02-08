class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        line = [0]*n
        for start, end, val in bookings:
            line[start-1] += val
            if end  < n:
                line[end] -=val
        for i in range(1,len(line)):
            line[i] += line[i-1]
        return line
        