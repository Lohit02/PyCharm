def getMinMaxDiff(arr, k):
    currSum = 0
    minSum = float("inf")
    maxSum = 0
    start = 0

    for i in range(len(arr)):
        currSum += arr[i]

        if (i - start + 1 == k):
            avg = currSum / k
            maxSum = max(avg, maxSum)
            minSum = min(maxSum, minSum)
            currSum -= arr[start]
            start += 1

    diff = maxSum - minSum
    return diff


arr = [3, 8, 9, 15]
k = 2
print(getMinMaxDiff(arr, k))