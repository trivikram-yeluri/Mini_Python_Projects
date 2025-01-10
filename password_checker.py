def password_checker(password):
    """This is the password complexity checker"""
    if len(password) < 8:
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char in '!.@#$%^&*()_-+=' for char in password):
        return False
    
    return True
passwd = input("Enter the password : ")
result = password_checker(passwd)
print(result)