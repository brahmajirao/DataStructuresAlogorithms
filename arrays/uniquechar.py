"""
Unique Characters in String
Problem
Given a string,determine if it is compreised of all unique characters.
For example, the string 'abcde' has all unique characters and should return True.
The string 'aabcde' contains duplicate characters and should return false.

Solution
We'll show two possible solutions, one using a built-in data structure and a built in function, and
another using a built-in data structure but using a look-up method to check if the characters are unique.
"""
def uni_char(string):
    return len(set(string)) == len(string)

def uni_char1(string):
    chars = set()
    for char in string:
        if char in chars:
            return False
        else:
            chars.add(char)
    return True

if __name__ == "__main__":
    print(uni_char("abcedfg k"))
    print(uni_char1("abcdefg kg"))