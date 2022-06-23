# is n a palindromic number?
def is_palindrome_num(n: int):
    if str(n) == str(n)[::-1]:
        return True
    return False

