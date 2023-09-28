#
# Complete the 'minMoves' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def minMoves(arr):
    # Write your code here
    lengthOfArr = len(arr)
    stepsCountRight = 0
    stepsCountLeft = 0

    wrongPlacedZerosRight = 0
    wrongPlacedZerosLeft = 0

    #right side
    for i in range(lengthOfArr - 1, -1, -1):
        if(arr[i] == 0):
            wrongPlacedZerosRight += 1
        else:
            stepsCountRight += wrongPlacedZerosRight

    #left side
    for i in range(0, lengthOfArr, 1):
        if(arr[i] == 0):
            wrongPlacedZerosLeft += 1
        else:
            stepsCountLeft += wrongPlacedZerosLeft

    return stepsCountLeft if stepsCountLeft < stepsCountRight else stepsCountRight
