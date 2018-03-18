
def count_vowels(str):
    vowels = str.count("a") + str.count("e") + str.count("i") \
             + str.count("o") + str.count("u")
    return vowels


def is_palindrome(str):
    is_palindrome_flag = True
    length = len(str)
    i = 0
    while(i < length//2):
        if(str[i] != str[length - i - 1]):
            is_palindrome_flag = False
            break
        i += 1
    return is_palindrome_flag


str = "hello olleh"
vowels = count_vowels(str)
print("Vowels in \"{}\" = {}\n".format(str, vowels))
is_palindrome_out = is_palindrome(str)
print("Is \"{}\" a palindrome? = {}\n".format(str, is_palindrome_out))
