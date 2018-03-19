
def count_vowels(str):
    """Function to count the number of vowels in a string

    Arguments:
        str {string} -- input string

    Returns:
        integer -- number of vowels in the input string
    """
    vowels = str.count("a") + str.count("e") + \
        str.count("i") + str.count("o") + str.count("u")
    return vowels


def is_palindrome(str):
    """Function to determine whether a string is a palindrome or not

    Arguments:
        str {string} -- input string

    Returns:
        boolean -- True if input string is a palindrome, else False
    """
    is_palindrome_flag = True
    length = len(str)
    for i in range(length//2):
        if(str[i] != str[length - i - 1]):
            is_palindrome_flag = False
            break
    return is_palindrome_flag


def word_count(str):
    """Function to count number of words in a string. Currently, this 
       function is limited to just space separated words and needs to 
       expanded to consider other punctuation characters.

    Arguments:
        str {string} -- input string

    Returns:
        integer -- number of words in a string
    """
    words = str.split(" ")
    return len(words)


# following is a test code, ideally needs to be converted to test cases
str = "hello ollehk"
vowels = count_vowels(str)
print("Vowels in \"{}\" = {}\n".format(str, vowels))
is_palindrome_out = is_palindrome(str)
print("Is \"{}\" a palindrome? = {}\n".format(str, is_palindrome_out))
word_cnt = word_count(str)
print("\"{}\" has {} words".format(str, word_cnt))
