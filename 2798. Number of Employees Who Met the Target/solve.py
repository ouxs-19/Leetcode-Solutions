class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        return reduce(lambda a, b: a + int(b >= target), hours, 0)