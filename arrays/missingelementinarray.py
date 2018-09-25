"""
Find the Missing Element
Problem:
Consider an array of non-negative integers.
A second array is formed by shuffling the elements of the first array and deleting a random element.
Given these two arrays, find which element is missing in the second array.

Here is an example input, the first array is shuffled and the number 5 is removed to construct the second array.

Input:

finder([1,2,3,4,5,6,7],[3,7,2,1,4,6])

Output:

5 is the missing number

Solution
The naive solution is go through every element in the second array and check whether it appears in the first array.
Note that there may be duplicate elements in the arrays so we should pay special attention to it.
The complexity of this approach is O(N^2), since we would need two for loops.

A more efficient solution is to sort the first array,
so while checking whether an element in the first array appears in the second,
we can do binary search (we'll learn about binary search in more detail in a future section).
But we should still be careful about duplicate elements. The complexity is O(NlogN).

If we don’t want to deal with the special case of duplicate numbers,
we can sort both arrays and iterate over them simultaneously.
Once two iterators have different values we can stop.
The value of the first iterator is the missing element. This solution is also O(NlogN)
"""


import collections
#bruit force solution
def finder1(arr1, arr2):
    dict = {}
    for item in arr1:
        if item in dict:
            dict[item] += 1
        else:
            dict[item] = 1

    for item in arr2:
        if item in dict:
            dict[item] -= 1

    for key in dict:
        if dict[key] > 0:
            return key



def finder2(arr1, arr2):
    dict = collections.defaultdict(int)
    for item in arr2:
        dict[item] += 1

    for item in arr1:
        if dict[item] == 0:
            return item
        else:
            dict[item] -= 1

from nose.tools import assert_equals
class TestFinder(object):

    def test(self):
        assert_equals(finder2([5,5,7,7], [5,7,7]), 5)
        assert_equals(finder2([1,2,3,4,5,6,7],[3,7,2,1,4,6]),5)
        assert_equals(finder2([9,8,7,6,5,4,3,2,1],[9,8,7,5,4,3,2,1]),6)
        print("all tests passed")

if __name__ == "__main__":
    test = TestFinder()
    test.test()