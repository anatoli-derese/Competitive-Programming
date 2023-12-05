class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        steps = 0
        c = capacity
        for i,plant in enumerate(plants):
            if plant <= capacity:
                steps += 1
                capacity -= plant
            else: 
                steps += 2 * i + 1
                capacity = c
                capacity -= plant
        return steps

        
       
            
                
        