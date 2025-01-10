def palindrome(string):
    """Check if a string is palindrome"""
    string = string.lower().replace(" ","")
    return string == string[::-1]
string = input("Enter a string : ")
print(palindrome(string))