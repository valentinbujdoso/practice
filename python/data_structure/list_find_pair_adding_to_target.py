# def sum_two(list, target):
#     res = sum_two_sub(list, target, list.pop())
#     if res:
#         return res
#
#     return sum_two_sub(list, target, list.pop())
#
#
# def sum_two_sub(list, target, first):
#     if first > target:
#         return
#
#     second = list.pop()
#
#     if first + second == target:
#         return [first, second]
#
#     return sum_two_sub(list, target, first)
#
#
#
# # print(sum_two([4, 2, 8, 1, 9], 3))
#
# n^2
# def iterative(list, target):
#     for i in range(len(list)):
#         if list[i] < target:
#             diff = target - list[i]
#             for j in range(i + 1, len(list)):
#                 if diff == list[j]:
#                     return [i, j]

# print(iterative([4, 2, 8, 1, 9], 3))


# time complexity nlogn
# space complexity
def nlogn(list, target):
    list.sort()
    min = 0
    max = len(list) - 1

    while min < max:
        sum = list[max] + list[min]
        if sum > target:
            max -= 1
        elif sum < target:
            min += 1
        else:
            return [list[min], list[max]]


# print(nlogn([4, 2, 8, 1, 9], 3))

# time complexiyt: 2n
def dict(list, target):
    dicta = {}
    for i in range(len(list)):
        if list[i] < target:
            dicta[list[i]] = i

    for element in dicta:
        temp = target - element
        if temp in dicta:
            return [dicta[temp], dicta[element]]

print(dict([4, 2, 8, 1, 9], 3))
