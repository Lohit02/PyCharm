from _ast import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(1, len(arr)):
            arr[i - 1] = self.giveGreatest(arr, i)

        arr[len(arr) - 1] = -1
        return arr

    def giveGreatest(self, arr: List[int], k) -> List[int]:
        maximun = -1
        for i in range(k, len(arr)):
            maximun = max(max, arr[i])

        return max;
