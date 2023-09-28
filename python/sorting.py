def bubble_sort(our_list): #n^2
    # We go through the list as many times as there are elements
    for i in range(len(our_list)):
        # We want the last pair of adjacent elements to be (n-2, n-1)
        for j in range(len(our_list) - 1):
            if our_list[j] > our_list[j+1]:
                # Swap
                our_list[j], our_list[j+1] = our_list[j+1], our_list[j]

####################################################################################
def bucketSort(array): # n+k, n^2, n
    bucket = []

    # Create empty buckets
    for i in range(len(array)):
        bucket.append([])

    # Insert elements into their respective buckets
    for j in array:
        index_b = int(10 * j)
        bucket[index_b].append(j)

    # Sort the elements of each bucket
    for i in range(len(array)):
        bucket[i] = sorted(bucket[i])

    # Get the sorted elements
    k = 0
    for i in range(len(array)):
        for j in range(len(bucket[i])):
            array[k] = bucket[i][j]
            k += 1
    return array


array = [.42, .32, .33, .52, .37, .47, .51]
print("Sorted Array in descending order is")
print(bucketSort(array))

####################################################################################
# Quick sort in Python

# function to find the partition position
def partition(array, low, high):

    # choose the rightmost element as pivot
    pivot = array[high]

    # pointer for greater element
    i = low - 1

    # traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:
            # if element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1

            # swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])

    # swap the pivot element with the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])

    # return the position from where partition is done
    return i + 1

# function to perform quicksort
def quickSort(array, low, high): #n log n, n^2
    if low < high:

        # find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)

        # recursive call on the left of pivot
        quickSort(array, low, pi - 1)

        # recursive call on the right of pivot
        quickSort(array, pi + 1, high)


data = [8, 7, 2, 1, 0, 9, 6]
print("Unsorted Array")
print(data)

size = len(data)

quickSort(data, 0, size - 1)

print('Sorted Array in Ascending Order:')
print(data)

####################################################################################


# example of merge sort in Python
# merge function take two intervals
# one from start to mid
# second from mid+1, to end
# and merge them in sorted order
def merge(Arr, start, mid, end) :

    # create a temp array
    temp[] = [0] * (end - start + 1)

    # crawlers for both intervals and for temp
    i, j, k = start, mid+1, 0

    # traverse both lists and in each iteration add smaller of both elements in temp
    while(i <= mid and j <= end) :
        if(Arr[i] <= Arr[j]) :
            temp[k] = Arr[i]
            k += 1; i += 1
        else :
            temp[k] = Arr[j]
            k += 1; j += 1

    # add elements left in the first interval
    while(i <= mid) :
        temp[k] = Arr[i]
        k += 1; i += 1

    # add elements left in the second interval
    while(j <= end) :
        temp[k] = Arr[j]
        k += 1; j += 1

    # copy temp to original interval
    for i in range (start, end+1) :
        Arr[i] = temp[i - start]


# Arr is an array of integer type
# start and end are the starting and ending index of current interval of Arr

def mergeSort(Arr, start, end):

    if(start < end) :
        mid = (start + end) / 2
    mergeSort(Arr, start, mid)
    mergeSort(Arr, mid+1, end)
    merge(Arr, start, mid, end)





####################################################################################
# Function to determine if a `target` exists in the sorted list `nums`
# or not using a binary search algorithm
def binarySearch(nums, target): #log n

    # search space is nums[left…right]
    (left, right) = (0, len(nums) - 1)

    # loop till the search space is exhausted
    while left <= right:

        # find the mid-value in the search space and
        # compares it with the target

        mid = (left + right) // 2

        # overflow can happen. Use:
        # mid = left + (right - left) / 2
        # mid = right - (right - left) // 2

        # target is found
        if target == nums[mid]:
            return mid

        # discard all elements in the right search space,
        # including the middle element
        elif target < nums[mid]:
            right = mid - 1

        # discard all elements in the left search space,
        # including the middle element
        else:
            left = mid + 1

    # `target` doesn't exist in the list
    return -1


if __name__ == '__main__':

    nums = [2, 5, 6, 8, 9, 10]
    target = 5

    index = binarySearch(nums, target)

    if index != -1:
        print('Element found at index', index)
    else:
        print('Element found not in the list')