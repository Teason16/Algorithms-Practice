'''
    Max Subset Sum No Adjacent:
    Given an array, what is the max number you can make (sum up)
    with the elements of the array without using and adjacent elements?

    Time:  O(N), where N is the number of nodes in the array
    Space (Best): O(1), when you use static variables to hold max sums

    Last Practiced: 2022-03-15 07:39:08
'''
def maxSubsetSumNoAdjacent(array):
    # If the input array is empty, 0 is the max value that can be returned
    if not len(array): return 0

    # Max a copy of the array to store max sums up to each index
    maxSums = array[:]

    # If the input array is one, the largest sum is array[0]
    if len(array) == 1: return array[0]

    # Manually set the max of the first two elements when: len(array) <= 2
    maxSums[1] = max(array[0], array[1])

    # Step through the rest of the array, calculating the max sum up to each given index
    for i in range(2, len(array)):
        maxSums[i] = max(maxSums[i-1], maxSums[i-2] + array[i])
    
    # Return the final index of maxSums (largest possible non-adjacent sum)
    return maxSums[len(maxSums) - 1]