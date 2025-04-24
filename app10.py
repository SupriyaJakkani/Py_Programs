#check given input is palindrome
def palindrome(name):
    if name == name[::-1]:
        return True
    else:
        return False
name1 = "Supriya"
name2 = "naman"
print(f"{name1} is palindrome: {palindrome(name1)}")
print(f"{name2} is palindrome: {palindrome(name2)}")


                 