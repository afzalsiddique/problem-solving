def is_palindrome_util(text, idx, n):
    if idx == n // 2:
        return True
    if text[idx] != text[-idx - 1]:
        return False
    else:
        return is_palindrome_util(text, idx + 1, n)

def is_palindrome(text):
    return is_palindrome_util(text, 0, len(text))

print(is_palindrome("madam"))
print(is_palindrome("abcd"))
print(is_palindrome("racecar"))
print(is_palindrome("abba"))
