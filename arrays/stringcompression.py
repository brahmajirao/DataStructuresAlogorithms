"""
String Compression
Problem
Given a string in the form 'AAAABBBBCCCCCDDEEEE' compress it to become 'A4B4C5D2E4'.
For this problem, you can falsely "compress" strings of single or double letters.
For instance, it is okay for 'AAB' to return 'A2B1' even though this technically takes more space.

The function should also be case sensitive, so that a string 'AAAaaa' returns 'A3a3'.

Solution
Since Python strings are immutable, we'll need to work off of a list of characters, and at the end convert
that list back into a string with a join statement.

The solution below should yield us with a Time and Space complexity of O(n).
Let's take a look with careful attention to the explanatory comments:
"""
def string_compression(string):
    r = ""
    l = len(string)
    if l ==0:
        return ""
    if l ==1:
        return string+'1'
    i = 1
    cnt = 1
    while i < l:
        if string[i] == string[i-1]:
            cnt += 1
        else:
            r = r+string[i-1]+str(cnt)
            cnt=1
        i+=1
    return r+string[i-1] + str(cnt)




if __name__ == "__main__":
    print(string_compression("AAAABBBBaaaAAAAAwweerrttKk"))