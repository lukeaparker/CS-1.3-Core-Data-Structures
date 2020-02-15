#!python

import string
# Hint: Use these string constants to ignore capitalization and/or punctuation
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase


def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing."""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str), 'input is not a string: {}'.format(text)
    # return is_palindrome_recursive(text, left=None, right=None)

def is_palindrome_iterative(text):
    O('n')
    # TODO: implement the is_palindrome function iteratively here
    text_len = len(text)
    index_start = 0
    index_stop = text_len - 1

    while index_start < index_stop:
        while text[index_start].isalpha() is False:
            index_start += 1

        #Decrement until alphabetic characters are hit
        while text[index_stop].isalpha() is False:
            index_stop -= 1

        if text[index_start].lower() != text[index_stop].lower():
            return False

        if text[index_start] != text[index_stop]:
            return False            
            
        index_start +=1
        index_stop -= 1 
    return True

    

def is_palindrome_recursive(text, left, right):
    'time complexity = O(n)'
    while left >= right:
        if text[left].isalpha == False:
            return is_palindrome_recursive(text, left+1, right)
        
        if text[right].isalpha == False:
            return is_palindrome_recursive(text, left, right-1)
        if text[left].lower() != text[right].lower():
                return print('false')
        else:
            return is_palindrome_recursive(text, left=left+1, right=right-1)
        return False





def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()
