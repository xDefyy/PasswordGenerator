import random

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#&%$€"
userchars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"

while 1:
    password_len = int(input("What lenght would you like your password to be : "))
    password_count = int(input("How many password do you want to have : "))
    for x in range(0,password_count):
        password = ""
        for x in range(0,password_len):
            password_char = random.choice(chars)
            password       = password + password_char
        print("Here is your password :", password)

    username_len = int(input("Please introduce the desired lenght of your username : "))
    username_count = int(input("Please introduce the desired amount of your usernames : "))
    for y in range(0,username_count):
        username = ""
        for y in range(0,username_len):
            username_char = random.choice(userchars)
            username      = username + username_char
        print("Here is your username ", username)
        break
    break
exit