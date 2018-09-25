
def rev_words1(str):
    return " ".join(reversed(str.split()))

def rev_words2(str):
    return " ".join(str.split()[::-1])

def sentence_reversal(str):
    lst_words = str.split()
    #print(lst_words)
    words_len = len(lst_words)
    reversed_string = ""
    while words_len > 0:
        reversed_string += lst_words[words_len-1] + ' '
        words_len -= 1
    return reversed_string.strip()


def rev_words(str):
    words = []
    length = len(str)
    space = [' ']
    i = 0
    while i<length:
        if str[i] not in space:
            word_start = i
            while i< len(str) and str[i] not in space:
                i += 1
            words.append(str[word_start:i])
        i+=1
    #print(words)
    return " ".join(reversed(words))



if __name__ == "__main__":
    print(rev_words('  Hi John, are you ready   to go?  '))
    print(rev_words2('Hi John, are you ready to go?'))
    print(sentence_reversal('Hi John, are you ready to go?'))