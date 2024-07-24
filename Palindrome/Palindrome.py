def isPalindrome(x: int):
    x = str(x)
    if x == x[::-1]:
        return True
    else :
        return False

x = int(input("enter an integr : "))
print(isPalindrome(x))