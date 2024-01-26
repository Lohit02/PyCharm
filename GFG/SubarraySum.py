class Solution:
    def subArraySum(self, arr, n, sum_):
        # Initialize curr_sum as
        # value of first element
        # and starting point as 0
        A = []
        curr_sum = arr[0]
        start = 0

        # Add elements one by
        # one to curr_sum and
        # if the curr_sum exceeds
        # the sum, then remove
        # starting element
        i = 1
        while i <= n:

            # If curr_sum exceeds
            # the sum, then remove
            # the starting elements
            while curr_sum > sum_ and start < i - 1:
                curr_sum = curr_sum - arr[start]
                start += 1

            # If curr_sum becomes
            # equal to sum, then
            # return true
            if curr_sum == sum_:
                A.append(start + 1)
                A.append(i)
                return A

            # Add this element
            # to curr_sum
            if i < n:
                curr_sum = curr_sum + arr[i]
            i += 1

        # If we reach here,
        # then no subarray
        A.append(-1)
        return A


class Main:
    def main(self):
        N = 10
        S = 15
        lst = []

        # number of elements as input
        n = int(input("Enter number of elements : "))

        # iterating till the range
        for i in range(0, n):
            ele = int(input())
            # adding the element
            lst.append(ele)

        ob = Solution()
        ans = ob.subArraySum(lst, N, S)

        for i in ans:
            print(i, end=" ")
        print()

    if __name__ == "__main__":
        main(self=None)
