"""
Create a function called word_split() which takes in a string phrase and a set list_of_words.
The function will then determine if it is possible to split the string in a way in which
words can be made from the list of words. You can assume the phrase will only contain words found
in the dictionary if it is completely splittable.

word_split('themanran',['the','ran','man'])
['the', 'man', 'ran']

word_split('ilovedogsJohn',['i','am','a','dogs','lover','love','John'])
['i', 'love', 'dogs', 'John']

word_split('themanran',['clown','ran','man'])
[]
"""

def word_split(phrase, list_words, output = None):
    # Checks to see if any output has been initiated.
    # If you default output=[], it would be overwritten for every recursion!
    if output is None:
        output = []

    # For every word in list
    for word in list_words:

        # If the current phrase begins with the word, we have a split point!
        if phrase.startswith(word):
            # Add the word to the output
            output.append(word)
            # Recursively call the split function on the remaining portion of the phrase--- phrase[len(word):]
            # Remember to pass along the output and list of words
            return word_split(phrase[len(word):], list_words, output)
    return output

if __name__ == "__main__":
    print(word_split('ilovedogsJohn',['i','am','a','dogs','lover','love','John']))