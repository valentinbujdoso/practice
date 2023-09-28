# You are given an array of positive numbers from 1 to n,
#  such that all numbers from 1 to n are present except one number x.
#  You have to find x. The input array is not sorted.
# Look at the below array and give it a try before checking the solution.

# 1 Runtime Complexity: Linear, O(n)
# Memory Complexity: Constant, O(1)

def missing_num(list):
    n = len(list) + 1
    actual_sum = (n*(n + 1)) / 2

    return actual_sum - sum(list)

print("missing_num: ", missing_num([2,3,4,5,6]))


# 2 Given an array of integers and a value, determine if there are any two integers
# in the array whose sum is equal to the given value.
#  Return true if the sum exists and return false if it does not.
#  Consider this array and the target sums:

# Runtime Complexity: Linear, O(n)
# Memory Complexity: Linear, O(n)

def find_sum_of_two(A, val):
    tmp_list = []
    for a in A:
        if val - a in tmp_list:
            return True

        tmp_list.append(a)

    return False


print("find_sum_of_two: ", find_sum_of_two([1,2,8,7,6,3], 5))


# 3 Given two sorted linked lists,
# merge them so that the resulting linked list is also sorted.
# Consider two sorted linked lists and the merged list below them as an example.

# Runtime Complexity: Linear, O(m+n) where m and n are lengths of both linked lists
# Memory Complexity: Constant, O(1)
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def merge_sorted(head1, head2):
    if head1 is None:
        return head2
    elif head2 is None:
        return head1


    mergedHead = None;

    if head1.value <= head2.value:
        mergedHead = head1
        head1 = head1.next
    else:
        mergedHead = head2
        head2 = head2.next

    mergedTail = mergedHead

    while head1 != None and head2 != None:
        temp = None
        if head1.value <= head2.value:
            temp = head1
            head1 = head1.next
        else:
            temp = head2
            head2 = head2.next

        mergedTail.next = temp
        mergedTail = temp

    if head1 != None:
        mergedTail.next = head1
    elif head2 != None:
        mergedTail.next = head2

    return mergedHead


def print_1(head):
    while(head):
        print(head.value, end=" ")
        head = head.next

head1 = Node(1)
head1.next = Node(2)
head1.next.next = Node(6)

head2 = Node(3)
head2.next = Node(4)
head2.next.next = Node(5)
head2.next.next.next = Node(7)

print("merge_sorted: ", print_1(merge_sorted(head1, head2)))


#  4 You are given a linked list where the node has two pointers.
#  The first is the regular next pointer.
#  The second pointer is called arbitrary_pointer and it can point
#  to any node in the linked list.
# Your job is to write code to make a deep copy of the given linked list.
#  Here, deep copy means that any operations on the original
# list should not affect the copied list.

# Runtime Complexity: Linear, O(n)
# Memory Complexity: Linear, O(n)

class Node4:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.arbitrary = None


def deep_copy_arbitrary_pointer(head):
    if head is None:
        return None

    current_head = head
    new_head = None
    new_tail = None
    ht = dict()

    while current_head is not None:
        node = Node4(current_head.value)
        node.arbitrary = current_head.arbitrary

        if new_head is None:
            new_head = node
        else:
            new_tail.next = node

        ht[current_head] = node

        new_tail = node
        current_head = current_head.next

    new_current = new_head

    while(new_current):
        if(new_current.arbitrary):
            node = ht[new_current.arbitrary]

            new_current.arbitrary = node

        new_current = new_current.next

    return new_head


#  5 Given the root of a binary tree, display the node values at each level.
#  Node values for all levels should be displayed on separate lines.
# Let’s take a look at the below binary tree.

# Runtime Complexity: Linear, O(n)
# Memory Complexity: Linear, O(n)

class Node5:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

from collections import deque

queued = []
visited = []

def level_order_traversal(root):
    if root == None:
        return
    result = ""
    queues = [deque(), deque()]

    current_queue = queues[0]
    next_queue = queues[1]

    current_queue.append(root)
    level_number = 0

    while current_queue:
        temp = current_queue.popleft()

        if temp.left != None:
            next_queue.append(temp.left)

        if temp.right != None:
            next_queue.append(temp.right)

        if not current_queue:
            result += str(temp.value)
            if next_queue:
                 result += "; "
            level_number += 1
            current_queue = queues[level_number % 2]
            next_queue = queues[(level_number + 1) % 2]
        else:
            result += str(temp.value) + ", "
    return result


root = Node5("1")
lfirst = Node5("2")
root.left = lfirst
lfirst.left = Node5("21")
lfirst.right = Node5("22")

root.right = Node5("3")
root.right.left = Node5("31")
root.right.right = Node5("32")

print("level_order_traversal: ", level_order_traversal(root))




#  Given a Binary Tree, figure out whether it’s a Binary Search Tree.
#  In a binary search tree, each node’s key value is smaller than the key value of
#  all nodes in the right subtree, and is greater than the key values of all nodes
#  in the left subtree. Below is an example of a binary tree that is a valid BST.

# Runtime Complexity: Linear, O(n)
# Memory Complexity: Linear, O(n)

class Node6:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def is_bst(root, min, max):
    if root is None:
        return True

    if root.value > max or root.value < min:
        return False

    # print(root.value)
    return is_bst(root.left, min, root.value) and is_bst(root.right, root.value, max)


root = Node6(15)
root.left = Node6(12)
root.right = Node6(10)
print("is_bst: ", is_bst(root, 0, 1000000000000000))

# 7 You are given a dictionary of words and a large input string.
# You have to find out whether the input string can be completely segmented into
#  the words of a given dictionary. The following two examples elaborate
# on the problem further.

# Runtime Complexity: Exponential, O(2^n)
#
# Memory Complexity: Polynomial, O(n^2)

def can_segment_string(s, dictionary):
    for i in range(1, len(s) + 1):
        first = s[0:i]
        if first in dictionary:
            second = s[i:]
            if not second or second in dictionary or can_segment_string(second, dictionary):
                return True
    return False

print("can_segment_string: ", can_segment_string("applepie", "apple apple pear pie"))


#  8 Reverse the order of words in a given sentence (an array of characters).
def reverse_words(sentence):    # sentence here is an array of characters
    splitted_sentence = sentence.split()
    result = ""
    while(splitted_sentence):
        result += splitted_sentence.pop()
        if splitted_sentence:
            result += " "

    return result

print("reverse_words", reverse_words("Hello World"))


#  9 Suppose we have coin denominations of [1, 2, 5] and the total amount is 7.
#  We can make changes in the following 6 ways:

# Runtime Complexity: Quadratic, O(m∗n)
# Memory Complexity: Linear, O(n)O

def solve_coin_change(denominations, amount):
    solution = [0] * (amount + 1)
    solution[0] = 1;
    for den in denominations:
        for i in range(den, amount + 1):
            solution[i] += solution[i - den]
        print(solution)

    return solution[len(solution) - 1]

print("solve_coin_change", solve_coin_change([1,2,5], 7))

#  10 Given a set of ‘n’ elements, find their Kth permutation.
#  Consider the following set of elements:

# Runtime Complexity: Linear, O(n)
# Memory Complexity: Linear, O(n)

def factorial(n):
        if n == 0 or n == 1:
            return 1
        return n * factorial(n -1 )

def find_kth_permutation(v, k, result):
    if not v:
        return

    n = len(v)
    # count is number of permutations starting with first digit
    count = factorial(n - 1)
    selected = (k - 1) // count

    result += str(v[selected])
    del v[selected]
    k = k - (count * selected)
    find_kth_permutation(v, k, result)

print("find_kth_permutation", find_kth_permutation([1,2,3], 5, []))

# 11 We are given a set of integers and we have to find all the possible subsets of
#  this set of integers. The following example elaborates on this further.

# Runtime Complexity: Exponential, O(2^n*n)
# Memory Complexity: Exponential, O(2^n*n)

def get_bit(num, bit):
    temp = (1 << bit)
    temp = temp & num
    if temp == 0:
        return 0
    return 1

def get_all_subsets(v, sets):
    subsets_count = 2 ** len(v)
    for i in range(0, subsets_count):
        st = set([])
        for j in range(0, len(v)):
            if get_bit(i, j) == 1:
                st.add(v[j])
        sets.append(st)

rest = []
get_all_subsets([1,2,3], rest)
print("get_all_subsets: ", rest)
#get_all_subsets:  [set(), {1}, {2}, {1, 2}, {3}, {1, 3}, {2, 3}, {1, 2, 3}]


# Task:
class Resolution:
    max_depth = 0

    def get_max_depth(self, array, position_x, position_y, level):

        max_row = len(array)
        max_column = len(array[0])

        if position_y not in range(0, max_column):
            return

        if position_x not in range(0, max_row):
            return

        if array[position_y][position_x] == "X":
            return

        if level > self.max_depth:
            self.max_depth = level

        array[position_y][position_x] = "X"

        self.get_max_depth(array, position_x + 1, position_y, level)
        self.get_max_depth(array, position_x - 1, position_y, level)
        self.get_max_depth(array, position_x, position_y + 1, level + 1)
        self.get_max_depth(array, position_x + 1, position_y + 1, level + 1)
        self.get_max_depth(array, position_x - 1, position_y + 1, level + 1)


list = [["X", ".", ".", ".", "X"],
        ["X", "X", "X", ".", "X"],
        [".", ".", ".", ".", "X"],
        [".", ".", ".", "X", "X"],
        ["X", "X", "X", ".", "X"]]

res = Resolution()


print("get_max_depth", res.get_max_depth(list, 1, 0, 0), res.max_depth + 1)