#!/usr/bin/env python3

def validate_user(username, minlen):
    """Checks if the received username matches the required conditions."""
    if type(username) != str:
        print("not a string")
        raise TypeError("username must be a string")
    if minlen < 1:
        print("minlen is too short")
        raise ValueError("minlen must be at least 1.")
    if len(username) < minlen:
        print("too short my dear..")
        return False
    if not username.isalnum():
        print("bad choice of characters!")
        return False
    # Usernames can't begin with a number
    if username [0].isnumeric():
        print("You can't start with a number.")
        return False
    return True

def main():
    minlen = 3;
    username = input("Enter username \n")
    if validate_user(username,minlen):
        print("Welcome", username)
    pass

main()
