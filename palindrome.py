def is_palindrome(s):
    return s == s[::-1] if len(s) > 1 else True