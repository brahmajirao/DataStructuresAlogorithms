"""
Reverse a String
This interview question requires you to reverse a string using recursion. Make sure to think of the base case here.

Again, make sure you use recursion to accomplish this. Do not slice (e.g. string[::-1]) or use iteration, there muse be a recursive call for the function.

Solution
In order to reverse a string using recursion we need to consider what a base and recursive case would look like. Here we've set a base case to be when the length of the string we are passing through the function is length less than or equal to 1.

During the recursive case we grab the first letter and add it on to the recursive call.
"""
def string_reversal(string):
    if len(string) <=1:
        return string
    else:
        return string_reversal(string[1:]) + string[0]


'''
RUN THIS CELL TO TEST YOUR FUNCTION AGAINST SOME TEST CASES
'''

from nose.tools import assert_equal


class TestReverse(object):
    def test_rev(self, solution):
        assert_equal(solution('hello'), 'olleh')
        assert_equal(solution('hello world'), 'dlrow olleh')
        assert_equal(solution('123456789'), '987654321')

        print('PASSED ALL TEST CASES!')


# Run Tests
test = TestReverse()
test.test_rev(string_reversal)