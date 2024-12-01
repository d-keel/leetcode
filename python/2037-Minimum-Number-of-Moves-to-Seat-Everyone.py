class Solution:
    def minMovesToSeat(self, seats: list[int], students: list[int]) -> int:
        ans: int = 0
        seats.sort()
        students.sort()

        for i in range(len(seats)):
            ans += abs(seats[i] - students[i])

        return ans
