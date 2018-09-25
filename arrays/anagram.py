"""
Anagram Solution
Problem
Given two strings, check to see if they are anagrams.
An anagram is when the two strings can be written using the exact same letters
(so you can just rearrange the letters to get a different phrase or word).

For example:

"public relations" is an anagram of "crap built on lies."

"clint eastwood" is an anagram of "old west action"

Note: Ignore spaces and capitalization. So "d go" is an anagram of "God" and "dog" and "o d g".

Solution
There are two ways of thinking about this problem, if two strings have the same frequency of letters/element
(meaning each letter shows up the same number of times in both strings) then they are anagrams of eachother.
On a similar vien of logic, if two strings are equal to each other once they are sorted,
then they are also anagrams of each other.
"""


#This is the easist way to chek whether two strings are anagram or not
#but not preferable in interviews
def anagram1(str1, str2):
    str1 = str1.replace(' ', '').lower()
    str2 = str2.replace(' ', '').lower()
    if sorted(str1) == sorted(str2):
        return True
    else:
        return False

def anagram2(str1, str2):
    str1 = str1.replace(' ', '').lower()
    str2 = str2.replace(' ', '').lower()

    #edge case check
    if len(str1) != len(str2):
        return False

    counter = {}

    for char in str1:
        if char in counter:
            counter[char] += 1
        else:
            counter[char] = 1

    for char in str2:
        if char in counter:
            counter[char] -= 1
        else:
            return  False

    for k in counter:
        if counter[k] != 0:
            return False

    return True


if __name__ == "__main__":
    print(anagram2("god", "dog"))

    print(anagram2("asdf", "dddd"))

