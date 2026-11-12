import numpy as np 

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        cars = [(p , (target - p) / s) for p, s in zip(position, speed)]

        cars.sort(reverse = True)

        fleets = 0 
        stack = []

        for pos, time in cars:
            if not stack or time > stack[-1]:
                fleets += 1
                stack.append(time)

        return fleets